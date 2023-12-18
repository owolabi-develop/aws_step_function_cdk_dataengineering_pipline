import boto3
import os



def handler(event,context):
   client = boto3.client('stepfunctions') 
   ## trigger aws step function state meachine
   step_function_state_machine_trigger = client.start_execution(
            stateMachineArn=os.environ['STATE_MECHINE_ARN']
            )
    