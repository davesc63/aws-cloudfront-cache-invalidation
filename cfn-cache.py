import boto3
import time
import os
import json

print("getting environment variable")
print("environment variable: " + os.environ['DISTRIBUTION_ID'])
dist = os.environ['DISTRIBUTION_ID'] # // get the Distribution ID from the lambda environment variable

def lambda_handler(event, context):
    client = boto3.client('cloudfront')
    invalidation = client.create_invalidation(
        DistributionId=dist,
        InvalidationBatch={
            'Paths': {
                'Quantity': 1,
                'Items': [
                    '/*', # // Update this section for specific paths
                ]
        },
        'CallerReference': str(time.time())
    })
    
    return {
        'statusCode': 200,
        'body': json.dumps('Successully created cache invalidation for ') + dist
    }
