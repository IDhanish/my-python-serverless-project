import json

def handler(event, context):
    if event["httpMethod"] == "GET":
        return {
            "statusCode": 200,
            "body": json.dumps(f"Hello from {event['path']} (GET)")
        }
    elif event["httpMethod"] == "POST":
        # Your common POST logic here
        response = {
            "statusCode": 200,
            "body": json.dumps(f"Hello from {event['path']} (POST)")
        }
        return response
