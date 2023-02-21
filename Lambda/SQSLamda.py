import boto3

# create a session with region
session = boto3.Session(region_name='us-east-1') # <-- Enter your current region which it may be different than mine

# create an SQS client
sqs = session.client('sqs')

# queue name
queue_name = 'BestWeek15Project' # <-- You can enter whatever name you would like

# creating the queue
response = sqs.create_queue(QueueName=queue_name)

# get the queue URL
queue_url = response['QueueUrl']

# print the URL of the created queue
print(f'Queue URL: {queue_url}')

