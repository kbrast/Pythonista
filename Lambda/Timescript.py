import boto3
import datetime
import json

def lambda_handler(event, context):
    # create an SQS client
    sqs = boto3.client('sqs')
    
    # define the queue URL
    queue_url = 'https://sqs.us-east-1.amazonaws.com/889958450895/BestWeek15Project' # <-- Enter your specific URL 
    
    # Ggt the current time
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # create the message to be sent
    message = {'time': current_time}
    
    # send the message to the SQS queue
    sqs.send_message(QueueUrl=queue_url, MessageBody=json.dumps(message))
    
    return {'statusCode': 200, 'body': 'Success My Friend'} # <-- You can enter any message you want to create
