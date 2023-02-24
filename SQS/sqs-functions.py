# SQS functions create and get queue

import boto3

def create_queue(sqs, QueueName):
    response = sqs.create_queue(
       QueueName=QueueName
    )
    
    print('Queue Created')
    
def get_queue_url(sqs, QueueName):
    response = sqs.get_queue_url(
    QueueName=QueueName
    )

    url = response['QueueUrl']
    
    print(url)
    return url
    
if __name__ == "__main__":
    sqs = boto3.client('sqs')
    QueueName = "Lambda-queue"
    create_queue(sqs, QueueName)
    get_queue_url(sqs, QueueName)