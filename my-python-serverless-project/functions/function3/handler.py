import json

def handler(event, context):
    if event["httpMethod"] == "GET":
        return {
            "statusCode": 200,
            "body": json.dumps("Hello from Function 3 (GET)")
        }
    elif event["httpMethod"] == "POST":
        # Your POST logic here
        response = {
            "statusCode": 200,
            "body": json.dumps("Hello from Function 3 (POST)")
        }
        return response
