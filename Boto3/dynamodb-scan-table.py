# Scan a DynamoDB table
# Use optional Filter Expression parameter to refine search

import boto3

from boto3.dynamodb.conditions import Key, Attr
dynamodb = boto3.resource('dynamodb')
table_name = dynamodb.Table('SuperBowl')
response = table_name.scan(
    FilterExpression=Attr('numero').begins_with('L')
)

print(response)