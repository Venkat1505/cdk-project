from aws_cdk.aws_ec2 import Vpc, Instance, InstanceType, InstanceClass, InstanceSize, AmazonLinuxImage
from constructs import Construct

class EC2Construct(Construct):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        # Create a VPC
        self.vpc = Vpc(self, "MyVpc", max_azs=2)

        # Create an EC2 instance
        self.instance = Instance(
            self,
            "MyInstance",
            instance_type=InstanceType.of(InstanceClass.T2, InstanceSize.MICRO),
            machine_image=AmazonLinuxImage(),
            vpc=self.vpc
        )
