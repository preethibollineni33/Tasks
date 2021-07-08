import logging
import boto3
from botocore.exceptions import ClientError

#List the buckets
def list_bucket():
    s3=boto3.client('s3')
    response=s3.list_buckets()

    print('Existing buckets')
    for bucket in response['Buckets']:
        print(f'{bucket["Name"]}')
list_bucket()