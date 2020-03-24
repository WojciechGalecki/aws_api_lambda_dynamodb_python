import boto3
import uuid
import os
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamoDb = boto3.resource('dynamodb')


def lambda_handler(event, context):
    logger.info('Adding new item to shopping list')
    logging.info(f'Input event: {event}')

    body = event['body']
    name = json.loads(body)['name']
    item = json.loads(body)['item']

    id = str(uuid.uuid4())

    logger.info(f'Name: {name}')
    logger.info(f'Item: {item}')
    logger.info(f'Id: {id}')

    table = dynamoDb.Table(os.environ['DYNAMODB_NAME'])
    table.put_item(
        Item={
            'name': name,
            'id': id,
            'item': item
        }
    )

    response = {'id': id}

    return {
        'statusCode': '201',
        'body': json.dumps(response),
        'headers': {
            'Content-Type': 'application/json'
        }
    }
