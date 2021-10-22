import boto3

ec2_client=boto3.client("ec2")

groupid="sg-082ad55fafb129d83"

ip_perm1=[
    {
        "FromPort":22,
        "ToPort":22,
        "IpProtocol":"tcp",
        "IpRanges":[
            {
                "CidrIp":"11.33.22.11/24",
                "Description":"SSH Open"
            }
        ]
    }
]

response=ec2_client.authorize_security_group_ingress(
    GroupId=groupid,
    IpPermissions=ip_perm1
)

print(response)