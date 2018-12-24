import json


def lambda_handler(event, context):
    response = {"test":"succeeded"}
    return {"statusCode": 200, "body": json.dumps(response)}
