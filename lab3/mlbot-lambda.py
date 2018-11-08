import json
 
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
 
def lambda_handler(event, context):
 
    params = json.loads(event['body'])
    if params['type'] == "url_verification":
        return success({'challenge': params['challenge']})
        
    return failure(Exception('Invalid event type: %s' % (params['type'])))
