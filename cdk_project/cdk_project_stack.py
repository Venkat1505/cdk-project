from aws_cdk import Stack
from constructs import Construct
from .s3_construct import S3Construct
from .ec2_construct import EC2Construct
from .lambda_construct import LambdaConstruct

class CdkProjectStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        # Add S3 Construct
        S3Construct(self, "S3Construct")

        # Add EC2 Construct
        EC2Construct(self, "EC2Construct")

        # Add Lambda Construct
        LambdaConstruct(self, "LambdaConstruct")
