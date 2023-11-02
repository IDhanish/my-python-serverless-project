import json

def handler(event, context):
    # Your function logic here
    response = {
        "statusCode": 200,
        "body": json.dumps("Hello from Function 3")
    }

    return response
