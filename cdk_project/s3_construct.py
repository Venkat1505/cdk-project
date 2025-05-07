from aws_cdk import RemovalPolicy
from aws_cdk.aws_s3 import Bucket
from constructs import Construct

class S3Construct(Construct):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        self.bucket = Bucket(
            self,
            "MyS3Bucket",
            versioned=True,
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True
        )
