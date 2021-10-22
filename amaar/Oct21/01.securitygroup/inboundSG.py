import boto3



ec2_client=boto3.client("ec2")

security_group_object=ec2_client.create_security_group(
    GroupName="amaar242424",
    Description="Amaar security group",
    VpcId="vpc-fd2df196"
)

print(security_group_object)

print("-----------------------------")

response=security_group_object.authorize_security_group_ingress( IpProtocol="tcp",ToPort=22,CidrIp="0.0.0.0/0")
print(response)