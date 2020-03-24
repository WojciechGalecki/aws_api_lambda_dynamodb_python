import boto3
import json

client = boto3.client('lambda')

response = client.invoke(
    FunctionName="demo-python",
    InvocationType="RequestResponse",
    Payload=json.dumps({"name": "test"})
)

res = json.loads(response['Payload'].read().decode('utf-8'))

print(res)
