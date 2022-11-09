import boto3

import logging

logger = logging.getLogger()

logger.setLevel(logging.INFO)

client = boto3.client('ecs')

def restart_service(event, context):
    cluster = "default"
    logger.info("Starting restart of services in {0} cluster".format(cluster))
    client.update_service(cluster=cluster, service="MyServiceName", forceNewDeployment=True)