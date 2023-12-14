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
    aws_s3_deployment as _deployment,
    RemovalPolicy,
    aws_lambda_event_sources
)
from constructs import Construct

ENVIRONMENT = {
    'STATE_MECHINE_ARN':"",
    "EXC_NAME":"customer_data_automation"
}
class AwsStepFunctionPiplineStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        lambda_function_role = _iam.Role(self,
                                         "lambdafunctionrole",
                                        assumed_by=_iam.ServicePrincipal("lambda.amazonaws.com"),
                                        managed_policies=[
                                            _iam.ManagedPolicy.from_aws_managed_policy_name("AmazonS3FullAccess"),
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
        
        
        raw_landing_bucket = _s3.Bucket(self,"rawlandingbucket",
                                        bucket_name='raw-landing-bucket',
                                         removal_policy=RemovalPolicy.DESTROY,
                                        auto_delete_objects=True,
                                        encryption=_s3.BucketEncryption.KMS)
        
        
        ### s3 bucket trigger   lambda_step_func_trigger
        lambda_step_func_trigger.add_event_source(
            aws_lambda_event_sources.S3EventSource(raw_landing_bucket,
                                                   events=[_s3.EventType.OBJECT_CREATED]))
        
        
        
        
        raw_staging_bucket = _s3.Bucket(self,"rawstagingbucket",
                                        bucket_name='staging-bucket',
                                         removal_policy=RemovalPolicy.DESTROY,
                                        auto_delete_objects=True,
                                        encryption=_s3.BucketEncryption.KMS)  
        
              
        
        consumptions_bucket = _s3.Bucket(self,"consumptionsbucket",
                                        bucket_name='consumptions-bucket',
                                         removal_policy=RemovalPolicy.DESTROY,
                                        auto_delete_objects=True,
                                        encryption=_s3.BucketEncryption.KMS)    

