# Snowflake Lambda Query Function

This Lambda function retrieves credentials from AWS Secrets Manager and uses them to connect to a Snowflake account. It runs a simple SELECT query to return the first 10 rows from a specified table.

## Setup

1. Create a secret in AWS Secrets Manager with the following keys:
   - account - Snowflake account name
   - user - Snowflake user name  
   - password - Password for the user

2. Create a Lambda function with the code from `snowflake_query.py`.

3. Configure the following environment variables on the Lambda function:
   - TABLE_NAME - Name of the Snowflake table to query  
   - DATABASE_NAME - Snowflake database name
   - SCHEMA_NAME - Schema that contains the table
   - WAREHOUSE_NAME - Snowflake virtual warehouse to use

4. Ensure the Lambda execution role has permission to call `secretsmanager:GetSecretValue`.

5. Set up necessary configuration to allow the Lambda function to connect to your Snowflake account.

## Usage

When the Lambda function is invoked, it will:

1. Retrieve the Snowflake credentials from Secrets Manager
2. Connect to the Snowflake account  
3. Execute a SELECT query to get the first 10 rows from the specified table
4. Return the results

The results are printed to CloudWatch Logs. To process the results further, you would need to add code to format the response.

## Troubleshooting

- Verify the Snowflake credentials in Secrets Manager are correct.
- Validate the Snowflake database, schema, warehouse, and table exist.
- Check the IAM permissions allow the Lambda to get secrets. 
- Ensure VPC is configured properly to allow connections to Snowflake.
