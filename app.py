#!/usr/bin/env python3
import os
import aws_cdk as cdk
from cdk_project.pipeline_stack import PipelineStack
from cdk_project.cdk_project_stack import CdkProjectStack

app = cdk.App()

# Only create pipeline when deploying manually
if app.node.try_get_context("deploy") != "app":
    PipelineStack(app, "PipelineStack",
        github_owner="Venkat1505",
        github_repo="cdk-project",
        github_branch="main",
        github_token_secret="GitHubTokenForCDK",
        env=cdk.Environment(account="088997610484", region="us-east-1")
    )

# Always deploy your main app stack from inside the pipeline
CdkProjectStack(app, "CdkProjectStack")

app.synth()
