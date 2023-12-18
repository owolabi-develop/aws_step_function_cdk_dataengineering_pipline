#!/usr/bin/env python3
import os

import aws_cdk as cdk


from glue.glue_stack import GlueCrawlerStack
from lambda_stack.lambda_stack import LambdaTriggerStack
from S3Bucket.s3bucket import S3bucketStacks
from step_function_stack.step_func_stack import Etl_StateMechineStack
from Sns.sns_stack import SnsStack

env_US = cdk.Environment(account="851725420683",region='us-east-1')
app = cdk.App()
GlueCrawlerStack(app,"GlueCrawlerStack",env=env_US)

LambdaTriggerStack(app,"LambdaTriggerStack",env=env_US)

S3bucketStacks(app,"S3bucketStacks")

Etl_StateMechineStack(app,"EtlStateMechineStack",env=env_US)

SnsStack(app,"SnsStack",env=env_US)

cdk.Tags.of(app).add("ProjectOwner","Owolabi akintan")
cdk.Tags.of(app).add("ProjectName","event driven elt pipline")


app.synth()
