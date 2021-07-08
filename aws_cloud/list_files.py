import logging
import boto3
from botocore.exceptions import ClientError

#List the files from the bucket
s3=boto3.resource('s3')
my_bucket=s3.Bucket('preethi33')

for files in my_bucket.objects.all():
    print(files.key)