# Remove item from a DynamoDB table

import boto3

dynamodb = boto3.resource('dynamodb')
table_name = dynamodb.Table('SuperBowl')
response = table_name.delete_item(
    Key={
        'numero':'XLVIII',
        'result':'Seattle 43, Denver 8'
    } 
)

print('Item successfully removed')