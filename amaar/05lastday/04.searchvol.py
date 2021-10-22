import boto3

AWS_REGION = "us-east-2"

ec2_resource = boto3.resource('ec2', region_name=AWS_REGION)

for volume in ec2_resource.volumes.filter(
    VolumeIds=[
        'vol-0075f8ef1cf617e12',
        'vol-0c49d1090104becca'
    ],
):
    print(f'Volume {volume.id} ({volume.size} GiB) -> {volume.state}')
