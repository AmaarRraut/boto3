import boto3
AWS_REGION="us-east-2"
 
ec2_resource=boto3.resource("ec2",region_name=AWS_REGION)
 
volumeCollection=ec2_resource.volumes.all()
 
for volume in volumeCollection:
    print(volume)