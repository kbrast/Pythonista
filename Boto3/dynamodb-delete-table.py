# Delete a DynamoDB table

import boto3

dynamodb = boto3.client('dynamodb')

response = dynamodb.delete_table(
    TableName="SuperBowl",
)

print("Table successfully deleted")
