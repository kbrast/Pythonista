# Create an SQS queue

import boto3

sqs = boto3.client('sqs')

response = sqs.create_queue(
    QueueName='RedLambdaQueue'
    )
    
print('Queue created')