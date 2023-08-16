import os
import json
import boto3
import snowflake.connector

def lambda_handler(event, context):

    # Get Snowflake credentials from Secrets Manager
    secrets_client = boto3.client('secretsmanager')
    secrets_response = secrets_client.get_secret_value(SecretId='snowflake_creds')
    creds = json.loads(secrets_response['SecretString'])
    
    # Get other config from environment variables
    table = os.environ['TABLE_NAME']
    database = os.environ['DATABASE_NAME']
    schema = os.environ['SCHEMA_NAME']
    warehouse = os.environ['WAREHOUSE_NAME']

    # Connect to Snowflake
    conn = snowflake.connector.connect(
        user=creds['user'],
        password=creds['password'],
        account=creds['account'],
        database=database,
        schema=schema,
        warehouse=warehouse
    )

    # Query for first 10 rows
    cs = conn.cursor()
    cs.execute(f"SELECT * FROM {table} LIMIT 10")

    # Fetch and print results
    rows = cs.fetchmany(10)
    print(rows)
    
    # Close connection
    cs.close()
    conn.close()

    return {
        'statusCode': 200,
        'body': json.dumps('Query successful!')
    }
