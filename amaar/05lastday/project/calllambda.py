import boto3,json
lambda_client=boto3.client("lambda")
test_event=dict()
FuncName="amaar3lambda"
response=lambda_client.invoke(
    FunctionName=FuncName,
    Payload=json.dumps(test_event)
)

print(response["Payload"])
print(response["Payload"].read().decode("utf-8"))
