import boto3
import json
import logging
import configparser
from src.settings import task_settings

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def create_dms_task(replication_instance_arn, source_endpoint_arn, target_endpoint_arn, task_settings, schema_name,
                    table_name, task_name, migration_type):
    try:
        # Initialize DMS client
        dms_client = boto3.client(
            'dms',
            aws_access_key_id=config['aws']['aws_access_key'],
            aws_secret_access_key=config['aws']['aws_secret_key'],
            region_name=config['aws']['region']
        )

        # Prepare table mappings
        table_mappings = {
            "rules": [
                {
                    "rule-type": "selection",
                    "rule-id": "1",
                    "rule-name": "1",
                    "object-locator": {
                        "schema-name": schema_name,
                        "table-name": table_name
                    },
                    "rule-action": "include"
                }
            ]
        }

        # Create replication task
        response = dms_client.create_replication_task(
            ReplicationTaskIdentifier=task_name,
            ReplicationInstanceArn=replication_instance_arn,
            SourceEndpointArn=source_endpoint_arn,
            TargetEndpointArn=target_endpoint_arn,
            MigrationType=migration_type,  # Specify both full-load and CDC
            TableMappings=json.dumps(table_mappings),
            ReplicationTaskSettings=json.dumps(task_settings)
        )

        logger.info(f"DMS task created successfully: {task_name}")
        # Uncomment below line if you want to log the response
        # logger.debug(json.dumps(response, indent=4, default=str))

    except Exception as e:
        logger.error(f"Error occurred while creating DMS task: {e}")
        raise  # Re-raise the exception for further handling


if __name__ == "__main__":
    # Read configurations from config file
    config = configparser.ConfigParser()
    config.read('config.config')

    # Retrieve configuration values
    replication_instance_arn = config.get('dms', 'replication_instance_arn')
    source_endpoint_arn = config.get('dms', 'source_endpoint_arn')
    target_endpoint_arn = config.get('dms', 'target_endpoint_arn')
    schema_name = config.get('schema', 'schema_name')
    table_name = config.get('schema', 'table_name')
    task_name = config.get('dms', 'task_name')
    migration_type = config.get('dms', 'migration_type')

    # Generate task settings
    task_settings = task_settings()

    # Create DMS task
    create_dms_task(replication_instance_arn,
                    source_endpoint_arn,
                    target_endpoint_arn,
                    task_settings,
                    schema_name,
                    table_name,
                    task_name,
                    migration_type)
