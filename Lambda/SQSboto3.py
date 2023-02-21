import boto3

# creating a SQS client
sqs = boto3.client('sqs')

# creating a standard SQS queue
queue_name = 'Best15WeekProject' # <-- Insert the queue name you would like
response = sqs.create_queue(QueueName=queue_name, Attributes={'QueueType': 'standard'})

# printing the URL of the created queue
queue_url = response['QueueUrl']
print(f'Queue URL: {queue_url}')
