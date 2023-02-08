#!/usr/bin/env python3

# Create a list of popular AWS Services
# The list should be empty initially
AWSList = []
print(AWSList)

# Populate the list using append or insert
AWSList.append('Aurora')
AWSList.append('CloudFront')
AWSList.append('CloudWatch')
AWSList.append('Cognito')
AWSList.append('DynamoDB')
AWSList.append('EKS')
AWSList.append('Kinesis')
AWSList.append('SageMaker')
AWSList.append('SNS')
AWSList.append('VPC')

# Print the list and the length of the list
print('AWS Services:', AWSList)
List_length = str(len(AWSList))
print('List length =', List_length)

# Remove two specific services from the list by name or index
del AWSList [2:4]

# Print the new list and the new length of the list
print('AWS Services:', AWSList)
List_length = str(len(AWSList))
print('Revised list length =', List_length)
