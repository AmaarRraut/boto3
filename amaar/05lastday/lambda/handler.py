import json

def lambda_handler(event,context):
    return {
        "statusCode":200,
        "body":json.dumps("Welcome to Python Lambda Boto3")
    }
