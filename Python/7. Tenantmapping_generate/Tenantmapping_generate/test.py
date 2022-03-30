import json

jf = open('output.json')

# jf = open('sample-test.json')

originalData = json.load(jf)

output_json = []

#Function to filter to get only Customer Live or Provisioning Tenants

def getCustomerLiveOrProvisioning(tenantObj):
    flagLive = False
    # print(tenantObj["attributes"])
    for row in tenantObj["attributes"]:
        if(row["objectTypeAttribute"]["name"]=="Status" and (row["objectAttributeValues"][0]["value"] == "CUSTOMER LIVE" or row["objectAttributeValues"][0]["value"] == "PROVISIONING")):
            flagLive = True
            break
    if(flagLive):
        return True
    else:
        return False

def getTenantDetails(objTenant):
    tenantData = {}
    for row in objTenant["attributes"]:
        if(row["objectTypeAttribute"]["name"]=="Status"):
            tenantData["status"] = row["objectAttributeValues"][0]["value"]
        if(row["objectTypeAttribute"]["name"]=="Name"):
            tenantData["name"] = row["objectAttributeValues"][0]["value"]
        if(row["objectTypeAttribute"]["name"]=="ID"):
            tenantData["tenant_id"] = row["objectAttributeValues"][0]["value"]
        if(row["objectTypeAttribute"]["name"]=="GWS CC ID"):
            tenantData["tenant_uuid"] = row["objectAttributeValues"][0]["value"]
        if(row["objectTypeAttribute"]["name"]=="Master Region"):
            tenantData["primaryLocation"] = row["objectAttributeValues"][0]["displayValue"]
    return tenantData


def customFilter(fdata):
    #Get Customer Live or provisioning tenants
    statusfilteredData = (list(filter(getCustomerLiveOrProvisioning, originalData["objectEntries"])))
    finalData = list(map(getTenantDetails,statusfilteredData))
    return finalData

# print(len(customFilter(originalData)))

with open('data.json', 'w') as outfile:  
	    json.dump(customFilter(originalData), outfile, indent=2)

# json.dumps(jsonData, indent=4, sort_keys=True)




# # siz = 0
# for row in livefilteredData:
#     print(row)
# print(len(livefilteredData))


# for row in jsonData["objectEntries"][0]["attributes"]:
#     if(row["objectTypeAttribute"]["name"]=="Status" and (row["objectAttributeValues"][0]["value"] == "CUSTOMER LIVE" or row["objectAttributeValues"][0]["value"] == "PROVISIONING")):
#         print(row)
    # if():#Getting Live customers

# print(len(jsonData["objectEntries"][0]["attributes"]))

# print(json.dumps(jsonData, indent=4, sort_keys=True))