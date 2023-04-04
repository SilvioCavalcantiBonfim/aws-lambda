import os
import boto3

AMI = os.environ["AMI"]
INSTANCE_TYPE = os.environ["INSTANCE_TYPE"]
KEY_NAME = os.environ["KEY_NAME"]
SUBNET_ID = os.environ["SUBNET_ID"]

EC2 = boto3.resources("ec2")

def lambda_handler(event, context):
    instance = EC2.create_instances(
        ImageId=AMI,
        InstanceType=INSTANCE_TYPE,
        KeyName=KEY_NAME,
        SubnetId=SUBNET_ID,
        MinCount=1,
        MaxCount=1
    )
    for i in instance:
        print(f'New instance created: {i.id}')