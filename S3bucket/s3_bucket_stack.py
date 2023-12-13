from aws_cdk import (
    Duration,
    Stack,
    aws_sqs as sqs,
    aws_lambda as _lambda,
    aws_dynamodb as ddb,
    aws_glue as _glue,
    aws_iam as _iam,
    aws_stepfunctions as _sfn,
    aws_stepfunctions_tasks as _task,
    aws_s3 as _s3,
    aws_sns as _sns,
    aws_s3_notifications as _sn,
    aws_s3_deployment as _deployment
)
from constructs import Construct

class AwsStepFunctionPiplineStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
