import boto3
import os
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamoDb = boto3.resource('dynamodb')


def lambda_handler(event, context):
    logger.info('Removing item from shopping list')
    logging.info(f'Input event: {event}')

    name = event['queryStringParameters']['name']
    id = event['queryStringParameters']['id']

    logger.info(f'Name: {name}')
    logger.info(f'Id: {id}')

    table = dynamoDb.Table(os.environ['DYNAMODB_NAME'])
    table.delete_item(
        Key={
            'name': name,
            'id': id
        }
    )

    response = {'result': 'OK'}

    return {
        'statusCode': '200',
        'body': json.dumps(response),
        'headers': {
            'Content-Type': 'application/json'
        }
    }
