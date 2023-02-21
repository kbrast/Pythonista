import boto3

from datetime import datetime
import json

def lambda_handler(event, context):

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S %p")

    sqs = boto3.resource('sqs')
    queue = sqs.Queue("https://sqs.us-east-1.amazonaws.com/889958450895/BestWeek15Project")
    queue.send_message(MessageBody=current_time)
    return {
        'statusCode': 200,
        'body': json.dumps(current_time)
    }

