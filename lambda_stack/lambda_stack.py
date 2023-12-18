from constructs import Construct
import aws_cdk as cdk

from aws_cdk import (
    aws_iam as _iam,
    Stack, 
    aws_s3 as _s3,
    aws_lambda as _lambda,
    Duration,
    aws_lambda_event_sources,
    RemovalPolicy
)




ENVIRONMENT = {
    'STATE_MECHINE_ARN':"arn:aws:states:us-east-1:851725420683:stateMachine:Customer_data",
}

class LambdaTriggerStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)
        
        
         
        lambda_function_role = _iam.Role(self,
                                         "lambdafunctionrole",
                                        assumed_by=_iam.ServicePrincipal("lambda.amazonaws.com"),
                                        managed_policies=[
                                            _iam.ManagedPolicy.from_aws_managed_policy_name("AWSStepFunctionsFullAccess"),
                                             _iam.ManagedPolicy.from_aws_managed_policy_name("CloudWatchFullAccess"),
                                        ]
                                         )
        
        lambda_step_func_trigger = _lambda.Function(
            self,
            "lambdastepfunctrigger",
             runtime=_lambda.Runtime.PYTHON_3_10,
            code=_lambda.Code.from_asset("lambda"),
            handler="lambda_trigger_func.handler",
            timeout=Duration.seconds(60),
            role=lambda_function_role,
            environment=ENVIRONMENT
        )
        
      
       ## raw  raw_landing_bucket 
        raw_landing_bucket = _s3.Bucket(self,"rawlandingbucket",
                                        bucket_name='customer-raw-landing-bucket',
                                         removal_policy=RemovalPolicy.DESTROY,
                                        auto_delete_objects=True,
                                        encryption=_s3.BucketEncryption.KMS)
        
        
        ### s3 bucket trigger   lambda_step_func_trigger
        lambda_step_func_trigger.add_event_source(
            aws_lambda_event_sources.S3EventSource(raw_landing_bucket,
                                                   events=[_s3.EventType.OBJECT_CREATED]))