import boto3

response=client.describe_db_instances(
    DBInstanceIdentifier="",
    Filters=[
        {
            "Name":"engine",
            "Values":["MySQL"]
        }
    ]
)

print(response)
