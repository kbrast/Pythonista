# Create an s3 bucket

import boto3

s3 = boto3.client("s3")

s3.create_bucket(Bucket="kwb-boto3-storage")