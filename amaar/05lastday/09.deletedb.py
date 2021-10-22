import boto3

client = boto3.client('rds')
response = client.delete_db_instance(
    DBInstanceIdentifier='amaar-db-instance-01',
    SkipFinalSnapshot=True
)
print(response)
