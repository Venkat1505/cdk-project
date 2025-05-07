from aws_cdk.aws_lambda import Function, Runtime, Code
from constructs import Construct

class LambdaConstruct(Construct):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        # Create a Lambda function
        self.function = Function(
            self,
            "MyLambdaFunction",
            runtime=Runtime.PYTHON_3_9,
            handler="handler.handler",
            code=Code.from_asset("lambda")  # Points to your Lambda code directory
        )
