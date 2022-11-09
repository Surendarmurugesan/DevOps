import boto3

import logging

logger = logging.getLogger()

logger.setLevel(logging.INFO)

client = boto3.client('ecs')

def lambda_handler(event, context):
    cluster = "ECS-prod-cluster"
    logger.info("Starting restart of services in {0} cluster".format(cluster))
    client.update_service(cluster=cluster, service="nginx-service", forceNewDeployment=True)