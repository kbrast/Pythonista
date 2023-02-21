import boto3

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('Table name') # <-- enter your table name

table.delete()