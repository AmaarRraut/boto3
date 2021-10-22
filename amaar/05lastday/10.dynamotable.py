import boto3

dynamodb=boto3.resource("dynamodb")

table =dynamodb.Table("AmaarTable")

with table.batch_writer() as batch:
    batch.put_item(Item={"Name":"B1","Email":"b1@nubeera.com"})
    batch.put_item(Item={"Name":"B2","Email":"b2@nubeera.com"})
    print(batch)
