from aws_cdk import (
    Duration,
    Stack,
    aws_lambda as _lambda,
    aws_glue as _glue,
    aws_iam as _iam,
    aws_s3 as _s3,
    aws_sns as _sns,
    aws_s3_notifications as _sn,
    aws_s3_deployment as _deployment,
    RemovalPolicy,
    aws_lambda_event_sources
)
from constructs import Construct


class S3bucketStacks(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
       
       
        ## raw  raw_landing_bucket 
        raw_landing_bucket = _s3.Bucket(self,"rawlandingbucket",
                                        bucket_name='raw-landing-bucket',
                                         removal_policy=RemovalPolicy.DESTROY,
                                        auto_delete_objects=True,
                                        encryption=_s3.BucketEncryption.KMS)
    
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
        
        


