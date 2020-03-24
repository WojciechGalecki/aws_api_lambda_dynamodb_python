import boto3
import os
import json
import logging
from boto3.dynamodb.conditions import Key, Attr

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamoDb = boto3.resource('dynamodb')


def lambda_handler(event, context):
    logger.info('Retrieving shopping list')
    logging.info(f'Input event: {event}')

    name = event['queryStringParameters']['name']

    logger.info(f'Name: {name}')

    table = dynamoDb.Table(os.environ['DYNAMODB_NAME'])
    items = table.query(KeyConditionExpression=Key('name').eq(name))

    return {
        'statusCode': '200',
        'body': json.dumps(items['Items']),
        'headers': {
            'Content-Type': 'application/json'
        }
    }
