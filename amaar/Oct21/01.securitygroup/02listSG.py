import boto3

ec2_client=boto3.client("ec2")

groupid="sg-082ad55fafb129d83"

response=ec2_client.describe_security_groups(
    GroupIds=[
        groupid
    ]
)

print(response)