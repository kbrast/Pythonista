# Create a new table in DynamoDB

import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'numero',
            'AttributeType': 'S',
        },
        {
            'AttributeName': 'result',
            'AttributeType': 'S',
        },
    ],
    KeySchema=[
        {
            'AttributeName': 'numero',
            'KeyType': 'HASH',
        },
        {
            'AttributeName': 'result',
            'KeyType': 'RANGE',
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits':10,
    },
    TableName='SuperBowl',
)

print('Table successfully created')
