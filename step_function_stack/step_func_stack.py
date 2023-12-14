from aws_cdk import (
    Duration,
    Stack,
    aws_lambda as _lambda,
    aws_glue as _glue,
    aws_iam as _iam,
    aws_stepfunctions as _sfn,
    aws_stepfunctions_tasks as _task,
    aws_sns as _sns,
    aws_s3_notifications as _sn,
)
from constructs import Construct

class Etl_StateMechineStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        lambda_function_role = _iam.Role(self,
                                         "lambdafunctionrole",
                                        assumed_by=_iam.ServicePrincipal("lambda.amazonaws.com"),
                                        managed_policies=[
                                            _iam.ManagedPolicy.from_aws_managed_policy_name("AmazonS3FullAccess"),
                                        ]
                                         )
        
      
        
        
        
