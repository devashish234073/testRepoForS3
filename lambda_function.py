import json

def lambda_handler(event, context):
    """
    Simple Lambda function that returns a greeting.
    """
    print(f"Received event: {json.dumps(event)}")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda! Your CloudFormation stack deployed me!')
    }
