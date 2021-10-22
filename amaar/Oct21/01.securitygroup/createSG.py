import boto3


ec2_client=boto3.client("ec2")

ec2_client.create_security_group(
    GroupName="amaar24",
    Description="Amaar security group",
    VpcId="vpc-fd2df196"
)

print(response)