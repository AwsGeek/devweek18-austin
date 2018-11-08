# Lab 5: Cleanup
 In this lab you will tear down all AWS resources created during this tutorial.

## Task 1: Lambda resources
Delete all Lambda functions used during this tutorial
1. Delete the **mlbot** and **mlclassify** functions: https://console.aws.amazon.com/lambda/home

## Task 2: SageMaker resources
Delete all SageMaker resources used during this tutorial
1. Delete **mlclassify** endpoints: https://console.aws.amazon.com/sagemaker/home#/endpoints
2. Delete **mlclassify** endpoint configs: https://console.aws.amazon.com/sagemaker/home#/endpointConfig
3. Delete **mlclassify** models: https://console.aws.amazon.com/sagemaker/home#/models
4. Stop, then delete **mlclassify** notebooks: https://console.aws.amazon.com/sagemaker/home#/notebooks

## Task 3: API Gateway resources
1. Delete **mlbot** APIs: https://console.aws.amazon.com/apigateway/home#/apis

## Task 4: IAM resources
1. Delete the **mlbot** and **mlclassify** roles: https://console.aws.amazon.com/iam/home#/roles

## Task 5: S3 resources
1. Delete the bucket you created: https://console.aws.amazon.com/s3
