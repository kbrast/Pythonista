# Search for s3 buckets

import boto3

# Create an S3 client
s3 = boto3.client('s3')

# Call the list_buckets method to get a list of all the buckets
response = s3.list_buckets()

# Get a list of all the bucket names
bucketlist = [bucket['Name'] for bucket in response['Buckets']]

# Print the bucket names
print(bucketlist)
