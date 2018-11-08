import json
import boto3

from botocore.vendored import requests
 
sage = boto3.Session().client(service_name='runtime.sagemaker') 
names = ['airbus-a320','boeing-747','dornier-328']

def lambda_handler(event, context):
   
    url = event["url"]

    # download image bytes
    bytes = requests.get(url).content
    
    # classify aircraft in the image
    response = sage.invoke_endpoint(EndpointName='<SageMaker Endpoint Name', 
                                   ContentType='application/x-image', 
                                   Body=bytes)
    scores = response['Body'].read()
    scores = json.loads(scores)

    aircraft = ""
    if max(scores) > 0.90:
        aircraft = names[scores.index(max(scores))]
    
    return {
        "statusCode": 200,
        "body": aircraft
    }
