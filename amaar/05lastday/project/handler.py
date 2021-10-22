import json
import os
import logging
import boto3

LOGGER=logging.getLogger()
LOGGER.setLevel(logging.INFO)

AWS_REGION=os.environ.get("AWS_REGION","ap-south-1")
DB_TABLE_NAME=os.environ.get("DB_TABLE_NAME","testpro")

S3_CLIENT=boto3.client("s3")
DYNAMODB_CLIENT=boto3.resource("dynamodb",region_name=AWS_REGION)
DYNAMODB_TABLE=DYNAMODB_CLIENT.Table(DB_TABLE_NAME)

def get_data_from_file(bucketName,keyName):
    response=S3_CLIENT.get_object(Bucket=bucketName,Key=keyName)
    content=response["Body"]
    data=json.loads(content.read())
    LOGGER.info("_____________________________")
    LOGGER.info("%s/%s file content: %s",bucketName,keyName,data)
    return data

def save_data_to_db(item):
    result=DYNAMODB_TABLE.put_item(Item=item)
    return result

def lambda_handler(event,context):
    for r in event["Records"]:
        s3_bucket_name=r["s3"]["bucket"]["name"]
        s3_file=r["s3"]["object"]["key"]
        data=get_data_from_file(s3_bucket_name,s3_file)
        for i in data:
            save_data_to_db(i)

    return {
        "statusCode":200,
        "body":json.dumps("We took Uploaded Object From s3 and Inserted into DynamoDB")
    }

    return {
        "statusCode":200,
        "body":json.dumps("Welcome to Python Lambda Boto3")
    }
