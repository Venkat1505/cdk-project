from aws_cdk import (
    Stack,
    SecretValue,
    aws_codepipeline as codepipeline,
    aws_codepipeline_actions as cpactions,
    aws_codebuild as codebuild,
)
from constructs import Construct

class PipelineStack(Stack):
    def __init__(self, scope: Construct, id: str,
                 github_owner: str,
                 github_repo: str,
                 github_branch: str,
                 github_token_secret: str,
                 **kwargs):
        super().__init__(scope, id, **kwargs)

        # Artifact for source output
        source_output = codepipeline.Artifact()

        # Artifact for build output (optional here)
        build_output = codepipeline.Artifact()

        # Define the pipeline
        pipeline = codepipeline.Pipeline(self, "CDKPipeline",
                                         pipeline_name="CDKProjectPipeline")

        # Source Stage
        source_action = cpactions.GitHubSourceAction(
            action_name="GitHub_Source",
            owner=github_owner,
            repo=github_repo,
            branch=github_branch,
            oauth_token=SecretValue.secrets_manager(github_token_secret),
            output=source_output,
            trigger=cpactions.GitHubTrigger.WEBHOOK
        )

        pipeline.add_stage(
            stage_name="Source",
            actions=[source_action]
        )

        # Build Stage using buildspec.yml
        build_project = codebuild.PipelineProject(
            self,
            "CDKBuildProject",
            build_spec=codebuild.BuildSpec.from_source_filename("buildspec.yml"),
            environment=codebuild.BuildEnvironment(
                build_image=codebuild.LinuxBuildImage.STANDARD_5_0,
                privileged=True
            )
        )

        build_action = cpactions.CodeBuildAction(
            action_name="CDK_Build_And_Deploy",
            project=build_project,
            input=source_output,
            outputs=[build_output]
        )

        pipeline.add_stage(
            stage_name="BuildAndDeploy",
            actions=[build_action]
        )
