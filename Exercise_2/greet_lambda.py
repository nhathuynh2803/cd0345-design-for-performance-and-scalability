import json

def lambda_handler(event, context):
    message = {
        "message": "Hello from Udacity!",
        "event": event
    }
    return {
        "statusCode": 200,
        "body": json.dumps(message)
    }
