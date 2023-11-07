import json

def handler(event, context):
    if event["httpMethod"] == "GET":
        return {
            "statusCode": 200,
            "body": json.dumps("Hello from Function 2 (GET)")
        }
    elif event["httpMethod"] == "POST":
        # Your POST logic here
        response = {
            "statusCode": 200,
            "body": json.dumps("Hello from Function 2 (POST)")
        }
        return response
