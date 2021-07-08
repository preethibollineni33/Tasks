import logging
import boto3
from botocore.exceptions import ClientError

#Fetching the contents from the file
def fetch_content():
    s3=boto3.resource('s3')
    my_bucket=s3.Bucket('preethi33')

    for files in my_bucket.objects.all():
        key=files.key
        body=files.get()['Body'].read()
        print(body)
fetch_content()