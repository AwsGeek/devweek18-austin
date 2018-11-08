import boto3
import json
import re
from botocore.vendored import requests

session = boto3.session.Session()
lmbda = session.client('lambda')

slackurl = 'https://slack.com/api/chat.postMessage'

def response(code, body):
    return {
        'statusCode': str(code),
        'body': body,
        'headers': { 'Content-Type': 'application/json'}
    }
 
def success(res=None):
    return response(200, json.dumps(res))
 
def failure(err):
    return response(400, err.message)
 
functions = { 'detect': '<mldetect function ARN>' } 
commands = '|'.join(functions.keys())
regex = '(%s)\s+<(.*)>' % commands

def lambda_handler(event, context):
 
    print(event)
    
    params = json.loads(event['body'])
    if params['type'] == "url_verification":
        return success(  {'challenge': params['challenge']} )

    if params['type'] == "event_callback":

        event = params['event']
        text = event['text']
        matches = re.search( regex, text, re.IGNORECASE)
        
        if matches:
            
            cmd = matches.group(1)
            url = matches.group(2)
            
            lres = lmbda.invoke(
                FunctionName = functions[cmd],
                InvocationType = 'RequestResponse',
                Payload = json.dumps({"url":url})
            )
            
            result = json.loads(lres['Payload'].read().decode('utf8'))

            data = {'token':'<Bot User OAuth Access Token>', 
                    'channel':event['channel'],
                    'thread_ts':event['ts'],
                    'text': result["body"] } 
              
            r = requests.post(url = slackurl, data = data)     
        
        return success()        
        
    return failure(Exception('Invalid event type: %s' % (params['type'])))
