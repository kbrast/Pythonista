# Get SQS Queue URL

import boto3

sqs = boto3.client('sqs')

response = sqs.get_queue_url(
    QueueName='RedLambdaQueue'
    )

url = response['QueueUrl']

print(url)