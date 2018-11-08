# Lab 3: Build a public interface
In this lab you will use AWS Lambda and Amazon API Gateway to create a public interface for your aircraft classifier.

## Task 1: Create a Lambda function
Create an AWS Lambda function that uses Amazon Rekognition to determine if there are any aircraft in an image
1. Browse to the AWS Lambda console to create a new function: https://console.aws.amazon.com/lambda/home#/create
2. Select the **Author from Scratch** option:

<p align="center"><img src="images/lab2-create-function-1.jpg"></p>

3. Fill out the following information for the Lambda function:
* Name: **mlbot**
* Runtime: **Python 3.6**
* Role: **Create a custom role**

<p align="center"><img src="images/lab2-create-function-2.jpg"></p>

4. Specify the following information for the IAM role, then click the **Allow** button to continue:
* IAM Role: **Create a new IAM Role**
* Role Name: **mlbot**

<p align="center"><img src="images/lab2-create-function-3.jpg"></p>

5. Click the **Create** function' button to finish:

<p align="center"><img src="images/lab2-create-function-4.jpg"></p>

## Task 2: Update the IAM role
Update the IAM role to allow invocation of the **mlclassify* Lambda function
1. Browse to the AWS IAM console to edit the **mlbot** IAM role: https://console.aws.amazon.com/iam/home#/roles/mlbot
2. Click on the **Add inline policy** button

<p align="center"><img src="images/lab2-update-iam-1.jpg"></p>

3. Click on the **JSON** tab and replace the existing policy with the following. Include the ARN of your **mldetect** Lambda function:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid" : "mlbot",
            "Effect": "Allow",
            "Action": "lambda:InvokeFunction",
            "Resource": [
                "<mlclassify Function ARN>"
            ]
        }
    ]
}
```
4. Click on the **Review policy** button to continue

<p align="center"><img src="images/lab2-update-iam-2.jpg"></p>

5. Name the policy **mlbot**, then click on the **Create policy** button to finish

<p align="center"><img src="images/lab2-update-iam-3.jpg"></p>

## Task 3: Update the Lambda function
Add boilerplate code to respond correctly when Slack verifies your endpoint 
1. Browse to the AWS Lambda console to edit the **mlbot** Lambda function: https://console.aws.amazon.com/lambda/home#/functions/mlbot
2. Replace the **lambda_function.py** template code with the following ([mlbot-lambda.py](mlbot-lambda.py)):
```
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
```
3. Click the **Save** button to finish

<p align="center"><img src="images/lab2-update-function-1.jpg"></p>

## Task 4: Create an API Gateway
Expose a publicc interface for your Lambda function
1. Browse to the AWS Lambda console to edit the **mlbot** Lambda function: https://console.aws.amazon.com/lambda/home#/functions/mlbot
2. Click on **API Gateway** in the **Add triggers** section

<p align="center"><img src="images/lab2-create-gateway-1.jpg"></p>

3. Configure the API Gateway trigger as follows, then click on the **Add** button to continue
* Pick an existing API, or create a new one: **Create a new API**
* Security: **Open**

<p align="center"><img src="images/lab2-create-gateway-2.jpg"></p>

4. Click the ‘Save’ button to finish

<p align="center"><img src="images/lab2-create-gateway-3.jpg"></p>

5. When complete, copy the API endpoint value for use in the next lab

<p align="center"><img src="images/lab2-create-gateway-4.jpg"></p>

## This is the end of the lab
