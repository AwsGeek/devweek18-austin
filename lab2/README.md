# Lab 2: Create a private interface
In this lab you will use AWS Lambda to create a private interfaace for your Amazon SageMaker endpoint

## Task 1: Create a Lambda function
Create an AWS Lambda function that uses Amazon SageMaker to classify an aircraft in an image
1. Browse to the AWS Lambda console to create a new function: https://console.aws.amazon.com/lambda/home#/create
2. Select the **Author from Scratch** option:

<p align="center"><img src="images/lab5-create-function-1.jpg"></p>

3. Fill out the following information for the Lambda function:
* Name: **mlclassify**
* Runtime: **Python 3.6**
* Role: **Create a custom role**

<p align="center"><img src="images/lab2-create-function-2.jpg"></p>

4. Specify the following information for the IAM role, then click the **Allow** button to continue:
* IAM Role: **Create a new IAM Role**
* Role Name: **mlclassify**

<p align="center"><img src="images/lab5-create-function-3.jpg"></p>

5. Click the **Create** function' button to finish:

<p align="center"><img src="images/lab5-create-function-4.jpg"></p>

## Task 2: Update the IAM role
Update the IAM role to allow invocation of the SageMaker InvokeEndpoint API
1. Browse to the AWS IAM console to edit the **mlclassify** IAM role: https://console.aws.amazon.com/iam/home#/roles/mlclassify
2. Click on the **Add inline policy** button

<p align="center"><img src="images/lab5-update-iam-1.jpg"></p>

3. Click on the **JSON** tab and replace the existing policy with the following. Replace ```<SageMaker Endpoint ARN>``` weith the ARN captured previously.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "mlclassify",
            "Effect": "Allow",
            "Action": "sagemaker:InvokeEndpoint",
            "Resource": "<SageMaker Endpoint ARN>"
        }
    ]
}
```
4. Click on the **Review policy** button to continue

<p align="center"><img src="images/lab2-update-iam-2.jpg"></p>

5. Name the policy **mlclassify**, then click on the **Create policy** button to finish

<p align="center"><img src="images/lab5-update-iam-3.jpg"></p>

## Task 3: Update the Lambda function
Update the Lambda Function classify an aircraft in an image using Amazon SageMaker InvokeEndpoint API
1. Browse to the AWS Lambda console to edit the **mlclassify** Lamda function: https://console.aws.amazon.com/lambda/home#/functions/mlclassify
2. Replace the **lambda_function.py** template code with the following ([mlclassify-lambda.py](mlclassify-lambda.py)). Replace ```<SageMaker Endpoint Name>``` with the name of your SageMaker endpoint.
```
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
    response = sage.invoke_endpoint(EndpointName='<SageMaker Endpoint Name>', 
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
```
3. Click the **Save** button to finish

<p align="center"><img src="images/lab5-update-function-1.jpg"></p>

## Task 4: Test the Lambda function
Create a test event and test your Lambda function 
1. Browse to the AWS Lambda console to edit the **mlclassify** Lamda function: https://console.aws.amazon.com/lambda/home#/functions/mlclassify
2. Click on the **Select a test event..** drop down and select **Configure test events**

<p align="center"><img src="images/lab5-test-function-1.jpg"></p>

3. Specify the following onformation for the test event:
* Event template: **Hello World**
* Event name: **mlclassify**
* Code:
```
{
  "url": "https://s3-us-west-2.amazonaws.com/awsgeek-devweek-austin/boeing-747.jpg"
}
```

<p align="center"><img src="images/lab5-test-function-2.jpg"></p>

4. Click on the **Create** button to continue

<p align="center"><img src="images/lab5-test-function-3.jpg"></p>

5. Click click on the **Test** button, then verify the output of the test matches the example output below

<p align="center"><img src="images/lab5-test-function-4.jpg"></p>

## This is the end of the lab
