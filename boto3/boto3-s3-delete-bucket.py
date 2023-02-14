# Delete s3 bucket

import boto3

s3 = boto3.client('s3')
bucket = 'kwc-boto3-storage'
response = s3.delete_bucket(Bucket=bucket)
