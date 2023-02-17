# Query a DynamoDB table

import boto3

from boto3.dynamodb.conditions import Key
dynamodb = boto3.resource('dynamodb')
table_name = dynamodb.Table('SuperBowl')
response = table_name.query(
    KeyConditionExpression=Key('numero').eq('LVII')
)

print("Query results: ")
for item in response['Items']:
    print(item)
