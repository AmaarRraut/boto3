import boto3
ec2=boto3.client("ec2")
 
response=ec2.describe_regions()
print(response["Regions"])
 
response=ec2.describe_availability_zones()
print(response["AvailabilityZones"])