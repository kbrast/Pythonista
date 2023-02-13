#%%

# create S3 Bucket using Boto3

import boto3

client = boto3.client("s3")

#%%

client.create_bucket(Bucket="kwb-boto3-bucket")