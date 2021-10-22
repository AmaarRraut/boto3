import boto3

class SGHelper:
    def __init__(self):
        self.ec2_client-boto3.client("ec2")
    def createSG(self,GName,VpcId="vpc-fd2df196"):
        response=self.ec2_client.create_security_group(
            GroupName=GName,
            Description="Mujahed Security Group here ",
            VpcId=VpcId
        )
        return response
    def getClientObject(self):
        return self.ec2_client

#DriverClass
sg=SGHelper()
groupName="AmaarRrautsg"
response=sg.createSG(GName=groupName)
print(response)