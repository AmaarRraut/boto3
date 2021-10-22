import boto3

iam_client=boto3.client("iam")
lambda_client=boto3.client("lambda")
print("Client Object Prepared")
zipped_code=None
with open("lambda.zip","rb") as f:
    zipped_code=f.read()

print("ZippedCode Object Prepared")
iam_role=iam_client.get_role(RoleName="lambdarole")

print("IAM Role Selected")

response=lambda_client.create_function(
    FunctionName="amaar3lambda",
    Runtime="python3.9",
    Role=iam_role["Role"]["Arn"],
    Handler="handler.lambda_handler",
    Code=dict(ZipFile=zipped_code),
    Timeout=300
)
print("______________________")
print(response)
