import json
import csv
import re
from datetime import datetime
import time
import requests
import urllib
import sys
import subprocess
from requests.auth import HTTPBasicAuth
import datetime
import configs
import tenant_config
import logging

logging.basicConfig(level=logging.DEBUG)
insight_base_url = "https://api.atlassian.com/jsm/insight/workspace/52411f35-b789-4422-b9d1-42d106977a7f/v1/"
insight_schema = "Service Catalog"
jira_user = "surendar.murugesan@genesys.com"
jira_password = "oH66amM1x7Xn0uiGBIqg915F"

# def ascii_encode_dict(data):
#     ascii_encode = lambda x: x.encode('utf-8') if isinstance(x, unicode) else x 
#     return dict(map(ascii_encode, pair) for pair in data.items())

def execute_jira_post_request(base_url,user,password,data,post_method):
	url = base_url
	with open('data.txt', 'w') as outfile:  
	    json.dump(data, outfile)
	f = open('output.txt', 'w')
	print(configs.getcurl(), "-X",post_method,"-u", user+":"+password, url,"-d","@data.txt","--header","Content-Type: application/json")
	subprocess.check_call([configs.getcurl(), "-X",post_method,"-u", user+":"+password, url,"-d","@data.txt","--header","Content-Type: application/json"],stdout=f)
	f.close
	f = open('output.txt', 'r')
	content = f.read()
	try:
		result = json.loads(content)
	except ValueError:
		result = None
	f.close
	return result

def execute_jira_get_request(base_url,user,password):
	url = base_url
	f = open('output.txt', 'w')
	print(configs.getcurl(), "-u", user+":"+password, "-X","GET","-H","Content-Type: application/json", url)
	subprocess.check_call([configs.getcurl(), "-u", user+":"+password, "-X","GET","-H","Content-Type: application/json", url],stdout=f)
	logging.info(url)
	f.close
	f = open('output.txt', 'r')
	content = f.read()
	try:
		result = json.loads(content)
	except ValueError:
		result = None
		logging.warn("REST call failure ")
		sys.exit()
	f.close
	return result

def insight_get_schema_id(schema_name):
	url = insight_base_url + "objectschema/list"
	res = execute_jira_get_request(url,jira_user,jira_password)
	if "values" in res:
		for schema in res["values"]:
			if schema["name"] == schema_name:
				return str(schema["id"])
	return None

def insight_get_object_types(schema_id):
	url = insight_base_url + "objectschema/" + schema_id + "/objecttypes/flat"
	res = execute_jira_get_request(url,jira_user,jira_password)
	return res

def insight_get_objects(object_types,schema_id,object_type_name):
	target_obj_type = None
	for object_type in object_types:
		if object_type["name"] == object_type_name:
			target_obj_type = str(object_type["id"])
	post_data = dict()
	post_data["objectSchemaId"] = schema_id
	post_data["objectTypeId"] = target_obj_type
	post_data["resultsPerPage"] = 500
	post_data["includeAttributes"] = "true"
	url = insight_base_url + "object/navlist/iql"
	retry = 5
	while retry > 0:
		logging.debug("Fetching %s data (%s tries left)", object_type_name, retry)
		res = execute_jira_post_request(url,jira_user,jira_password,post_data,"POST")
		if res is not None:
			return res
		retry = retry - 1

def get_single_attr_value(attr_list,attr_name):
	for attr in attr_list:
		if attr["objectTypeAttribute"]["name"] == attr_name:
			if len(attr["objectAttributeValues"]) == 1:
				return attr["objectAttributeValues"][0]["value"]
			else:
				return None
	return None

def get_user_attr_value(attr_list,attr_name):
	for attr in attr_list:
		if attr["objectTypeAttribute"]["name"] == attr_name:
			if len(attr["objectAttributeValues"]) == 1:
				return attr["objectAttributeValues"][0]["user"]["displayName"]
			else:
				return None
	return None

def get_single_ref_value(attr_list,attr_name, attr_key):
	if(not attr_key):
		attr_key = "value"
	for attr in attr_list:
		if attr["objectTypeAttribute"]["name"] == attr_name:
			if len(attr["objectAttributeValues"]) == 1:
				# return attr["objectAttributeValues"][0]["referencedObject"]["objectKey"]
				return attr["objectAttributeValues"][0][attr_key]
			else:
				return None
	return None

def get_multiple_ref_value(attr_list,attr_name):
	ret = ""
	for attr in attr_list:
		if attr["objectTypeAttribute"]["name"] == attr_name:
			for attr_value in attr["objectAttributeValues"]:
				if ret != "":
					ret = ret + ","
				ret = ret + attr_value["referencedObject"]["objectKey"]
	return ret

def get_row(res_hash, key, value):
	res = next((l for l in res_hash["objectEntries"] if l[key] == value), None)
	return res

def get_regions(gen_reg_res, dep_reg_res, master_region, tenant_sc_id):
	master = get_row(gen_reg_res, 'objectKey', tenant_sc_id)
	master_region = get_single_attr_value(master["attributes"], "Name")
	result = {}
	result["master"] = master_region
	dep_reg = []
	for reg in dep_reg_res["objectEntries"]:
		if get_single_ref_value(reg["attributes"],"Key", "value") == tenant_sc_id:
			dep_reg.append(reg)
	dep_result = []
	for l in dep_reg:
		tmp_hsh={}
		# tmp_hsh = { "DeploymentType": get_single_attr_value(l["attributes"],"Redundancy Type"), "PrimaryRegion": get_single_ref_value(l["attributes"],"Primary Voice Region SIPS", "name"), "SecondaryRegion": get_single_ref_value(l["attributes"],"Secondary Voice Region SIPS", "name")}
		tmp_hsh = {"ors_p": get_single_ref_value(l["attributes"],"Primary Voice Region SIPS", "name"), "ors_b": get_single_ref_value(l["attributes"],"Secondary Voice Region SIPS", "name"), "gvp_p":get_single_ref_value(l["attributes"],"Primary GVP Region", "name"), "gvp_b":get_single_ref_value(l["attributes"],"Secondary GVP Region", "name")}
		dep_result.append(tmp_hsh)
	result["regions"] = dep_result
	return result

def get_das_regions(region_map):
	region_list = []
	das_regions = []
	for region in region_map:
		region_list = region_list + list(set(region.values()) - set(region_list))
	for region in region_list:
		l = region_iu_map(region)
		if l is not None:
			das_regions.append(region_iu_map(region))
	return das_regions

def get_dep_regions(dep_reg_res, tenant_sc_id, tenant_name, tenant_type):
	# To get all locations data(Primary and Secondary of SIPS and GVP)
	# Regions will be converted with reference to region map region_iu_map()
	dep_reg = []
	for reg in dep_reg_res["objectEntries"]:
		tmp = get_single_ref_value(reg["attributes"],"Tenant", "referencedObject")
		if tmp and tmp["objectKey"] == tenant_sc_id:
			dep_reg.append(reg)
	dep_result = set()
	for l in dep_reg:
		for key in ["Primary Voice Region SIPS","Secondary Voice Region SIPS","Primary GVP Region","Secondary GVP Region"]:
			tmp_region = get_single_ref_value(l["attributes"],key, "displayValue")
			if(tmp_region != None):
				dep_result.add(region_iu_map(tmp_region,tenant_name,tenant_type))
	return dep_result


def region_iu_map(region,tenantName,tenantType):
	# returns region in reference to region map of config
	# if Microsoft IQR and Hartford Life Insurance are both large tenant type, then dedicated regions will be fetched
	# configs.region_map -> regular and configs.region_map_large_tenants -> large type
	dedicatedCustomers = ["Microsoft IQR","Hartford Life Insurance"]
	dedicatedRegions = ["us-west-2","us-east-2"]
	typeRegionMap = configs.region_map_large_tenants if (tenantType == "large") else configs.region_map
	if tenantName in dedicatedCustomers and region in dedicatedRegions:
		if region in typeRegionMap.keys():
			return typeRegionMap[region][tenantName]
	elif region in typeRegionMap.keys():
		return typeRegionMap[region]
	else:
		return region	

def get_bucket_path(region):
    for breg in configs.bucketRegions:
        if region in breg["regionValues"]:
            return breg["name"]
    return None

def get_jira_api_tenants():
	# Read Insight schema
	schema_id = insight_get_schema_id(insight_schema)
	object_types = insight_get_object_types(schema_id)
	# Read Tenant, Deployment Regions and Genesys Regions schemas
	res = insight_get_objects(object_types,schema_id,"Service Instance")
	dep_reg_res = insight_get_objects(object_types,schema_id,"Deployment Region")
	gen_reg_res = insight_get_objects(object_types,schema_id,"Genesys Region")
	tenant_res = insight_get_objects(object_types,schema_id,"Tenant")
	logging.debug("%s %s %s %s", (res is None),(dep_reg_res is None),(gen_reg_res is None),(tenant_res is None))
	if res is None or dep_reg_res is None or gen_reg_res is None or tenant_res is None:
		now = datetime.datetime.now()
		logging.error(" Error in fetching data from JIRA server: %s", now)
		exit(0)
	# with open('res.json', 'r') as infile:  
	# 	res = json.load(infile)
	# with open('dep_reg_res.json', 'r') as infile:  
	# 	dep_reg_res = json.load(infile)
	# with open('gen_reg_res.json', 'r') as infile:  
	# 	gen_reg_res = json.load(infile)
	# with open('tenant_res.json', 'r') as infile:  
	# 	tenant_res = json.load(infile)
	tenant_list = []
	for row in tenant_res["objectEntries"]:
		rowStatus =  get_single_attr_value(row["attributes"],"Status")
		# print('RowStatus'+rowStatus)
		if rowStatus != 'TERMINATED':#allow only non terminated one
			tmp_hsh = {}
			tenant_sc_id = get_single_ref_value(row["attributes"],"Key", "value")
			tenant_name = get_single_ref_value(row["attributes"],"Name", "value")
			tenant_Status = get_single_attr_value(row["attributes"],"Status")
			tenant_ccid = get_single_ref_value(row["attributes"],"GWS CC ID", "value")
			tenant_id = get_single_ref_value(row["attributes"],"ID", "value")
			tenant_master = get_single_ref_value(row["attributes"],"Master Region", "displayValue")
			if(tenant_id != None):
				tmp_hsh = {"name": tenant_name, "status": tenant_Status,"tenant_uuid": tenant_ccid, "tenant_id":tenant_id,"primaryLocation":tenant_master}#, "label": row['label']}
				if tenant_id in tenant_config.large_tenants:
						tmp_hsh["type"] = "large"
				else:
					tmp_hsh["type"] = "regular"
				
				if tenant_id in tenant_config.test_tenants:
					continue
				tmp_hsh["locations"] = list(get_dep_regions(dep_reg_res, tenant_sc_id,tmp_hsh["name"], tmp_hsh["type"]))
				if(tmp_hsh["primaryLocation"]):
					shortbregion = tmp_hsh["primaryLocation"].split("-")[0]
					tmp_hsh["bucket_region"] = get_bucket_path(shortbregion)
				tmp_hsh["primaryLocation"] =region_iu_map(tmp_hsh["primaryLocation"],tmp_hsh["name"],tmp_hsh["type"])
				tenant_list.append(tmp_hsh)
	return tenant_list

def generate_tenantmapping_file():
	tenant_list = get_jira_api_tenants()
	with open('tenantmapping.json', 'w') as fp:
	    json.dump(tenant_list, fp, indent=4, sort_keys=True)

def tenantmappingfile():
	now = datetime.datetime.now()
	logging.info('Refreshing tenantmapping.json file at %s', now)
	parsed_hash = generate_tenantmapping_file()
	logging.info("Generated tenantmapping: %s", now)
	return parsed_hash

generate_tenantmapping_file()