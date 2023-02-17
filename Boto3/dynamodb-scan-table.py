# Scan a DynamoDB table

import boto3

from boto3.dynamodb.conditions import Key, Attr
dynamodb = boto3.resource('dynamodb')
table_name = dynamodb.Table('SuperBowl')
response = table_name.scan(
    FilterExpression=Attr('numero').begins_with('L')
)

print(response)