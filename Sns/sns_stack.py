from aws_cdk import (
    Stack,
    aws_sns as _sns,
    aws_sns_subscriptions as subscription
)
from constructs import Construct

class SnsStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        
        ## create sns topic to send message to admin affter job finished
        send_email = _sns.Topic(self,"sendEmail",topic_name='job-completed')
        
        ## subscribe to the topic to recieve message
        send_email.add_subscription(subscription.EmailSubscription('owolabidevelop84@gmail.com'))
        
      
        
        
        
