# In shell:
    # Get the Tenant whitelist file, - done
# In Python:
    # 1 by 1 tenantid getting from list, 
    # search tenant in log file, 
    # next line on tenant id,
    # building filelist with process id,
    # search with process id to find is completed or not.





import json
import os
import fileinput

STACK_NAME="DAS-E4-USW9-DEVOPS"
PROMETHEUS_DATASOURCE = "vm-prometheus-usw1"

if 'DAS' in STACK_NAME:
    template = "DAS-grafana-template.json"
elif 'DES' in STACK_NAME:
    template = "DES-grafana-template.json"
else:
    print("cannot find grafana template for stack: "+STACK_NAME+", please check your stack name")

with open(template, 'r') as file :
  filedata = file.read()

filedata = filedata.replace("<STACK_NAME>", STACK_NAME)
filedata = filedata.replace("<PROM_DATA_SOURCE>",PROMETHEUS_DATASOURCE )

with open(STACK_NAME+"-dashboard.json", 'w') as outfile:
    outfile.write(filedata)