from aws_cdk import (
    Duration,
    Stack,
    aws_lambda as _lambda,
    aws_glue as _glue,
    aws_iam as _iam,
    aws_stepfunctions as _sfn,
    aws_stepfunctions_tasks as _tasks,
    aws_sns as _sns,
    aws_s3_notifications as _sn,
    aws_s3 as _s3,
    aws_logs as logs
)
from constructs import Construct


#cdksns_topic_arn = "arn:aws:sns:us-east-1:851725420683:job-completed"
class Etl_StateMechineStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        Customer_data_role = _iam.Role(self,"Customer_data_role",
                                       assumed_by=_iam.ServicePrincipal("states.amazonaws.com"),
                                        managed_policies=[
                                             _iam.ManagedPolicy.from_aws_managed_policy_name("AWSGlueConsoleFullAccess"),
                                              _iam.ManagedPolicy.from_aws_managed_policy_name("AmazonAthenaFullAccess"),
                                               _iam.ManagedPolicy.from_aws_managed_policy_name("AmazonSNSFullAccess"),
                                             _iam.ManagedPolicy.from_aws_managed_policy_name("CloudWatchFullAccess"),
                                        ])
        
        Customer_data = _sfn.StateMachine(self, "CustomerData",
                                          role=Customer_data_role,          
            definition_body=_sfn.DefinitionBody.from_file("aws_asl/pipline_aws_step_function_state_language.asl.json")
        )
                
#         ### start state 1
#         start_glue_crawler = _tasks.GlueStartCrawlerRun(self, "startgluecrawlerTasks",
#                                 crawler_name="customer_crawler",
#                                 comment="start glue crawler to crawl s3 customer data table")
        
#         ## custom state check glue crawler  2
        
#         get_glue_crawler_status_json = {
#                     "Type": "Task",
#                     "Parameters": {
#                         "Name": "customer_crawler"
#                     },
#                     "Resource": "arn:aws:states:::aws-sdk:glue:getCrawler"
#                     }
        
        
        
#        ## custom glue crawler status 2
#         get_glue_crawler_status = _sfn.CustomState(self,
#                                                      "checkGlue_CrawlerStatus",
#                                                      state_json=get_glue_crawler_status_json)
        
        
#         ## check custom glue crawler status 3
        
#         check_glue_crawler_status = _sfn.Choice(self,
#                                                "CheckGlueCrawlerStatus")
        
#          ## wait for clawler for 30 seconds when state status is RUNNING
#         wait_for_glue_crawler_status = _sfn.Wait(self,"WaitForGlueCrawlerStatus",
#                                                  time=_sfn.WaitTime.duration(Duration.seconds(30)))
       
#         ## check for crawler state RUNNING
#         check_glue_crawler_status.when(_sfn.Condition.string_equals('$.Crawler.State','RUNNING'),wait_for_glue_crawler_status)
        
        
#          ## if crawler is on ready state start athena query
#         start_query_execution_job = _tasks.AthenaStartQueryExecution(self, "StartAthenaQuery",
#             query_string="select * from customers;",
#             query_execution_context=_tasks.QueryExecutionContext(
#                 database_name="customer-database"
#             ),
#             result_configuration=_tasks.ResultConfiguration(
#                 encryption_configuration=_tasks.EncryptionConfiguration(
#                     encryption_option=_tasks.EncryptionOption.S3_MANAGED
#                 ),
#                 output_location=_s3.Location(
#                     bucket_name="query-results-bucket",
#                     object_key="result"
#                 )
#             ))
        
        
#         ## check for crawler state READY
#         check_glue_crawler_status.when(_sfn.Condition.string_equals('$.Crawler.State','READY'),start_query_execution_job)
        
       
        
        
#         ## get athena query result 
#         get_query_results_job = _tasks.AthenaGetQueryResults(self, "GetQueryResults",
#          query_execution_id=_sfn.JsonPath.string_at("$.QueryExecutionId")
#         )
        
        
#         publish_athena_message_to_admin = _tasks.SnsPublish(self, "Publish message to admin",
#         topic=_sns.Topic.from_topic_arn(self,"message To admin",topic_arn=sns_topic_arn),
#         message=_sfn.TaskInput.from_json_path_at("$.QueryExecutionId"),
#         result_path="$.sns"
# )
        
        
#         ## start glue Job run
#         start_gluejobscript_run = _tasks.GlueStartJobRun(self,
#                                                          "start gluejob script run",
#                                                          glue_job_name='customer_data_job',
#                                                           integration_pattern=_sfn.IntegrationPattern.RUN_JOB)
        
#         ## check for crawler state READY to trigger glue job
#         check_glue_crawler_status.when(_sfn.Condition.string_equals('$.Crawler.State','READY'), start_gluejobscript_run)
        
        
        
        
#         ## get glue Job run status  custome json
        
#         glue_jobrun_status_json = {
#                 "Type": "Task",
#                 "Next": "Check Glue JobRun state Status",
#                 "Parameters": {
#                     "JobName": "customer_data_job"
#                 },
#                 "Resource": "arn:aws:states:::aws-sdk:glue:getJob"
#                 }
        
#         ## get glue Job run status 
#         get_glue_job_run_status = _sfn.CustomState(self,
#                                                    "get glue jobrunstatus",
#                                                    state_json=glue_jobrun_status_json
#                                                    )
        
        
        
#         ##  check glue job run status
#         check_glue_job_status = _sfn.Choice(self,
#                                                "CheckGluejobStatus")
        
#         publish_glueJob_message_to_admin = _tasks.SnsPublish(self, "Publish message to admin",
#         topic=_sns.Topic.from_topic_arn(self,"message To admin",topic_arn=sns_topic_arn),
#         message=_sfn.TaskInput.from_json_path_at("$.JobRun.JobRunState"),
#         result_path="$.sns"
# )
        
#         ## check if glue job status has SUCCEEDED
#         check_glue_job_status.when(_sfn.Condition.string_equals('$.JobRun.JobRunState','SUCCEEDED'),publish_glueJob_message_to_admin)
        
        
#          ## check if glue job status has FAILED
#         check_glue_job_status.when(_sfn.Condition.string_equals('$.JobRun.JobRunState','FAILED'), publish_glueJob_message_to_admin)
        
        
    
        
        
#         ## state mechine defination
#         definition = _sfn.Chain.start(start_glue_crawler)\
#             .next(get_glue_crawler_status)\
#             .next(check_glue_crawler_status)\
#             .next(wait_for_glue_crawler_status)\
#             .next(start_query_execution_job)\
#             .next(get_query_results_job)\
#             .next(publish_athena_message_to_admin)\
#             .next(start_gluejobscript_run)\
#             .next(get_glue_job_run_status)\
#             .next(check_glue_job_status)\
#             .next(publish_glueJob_message_to_admin)
            
        
#         customer_log_group = logs.LogGroup(self, "customer log group")
        
#         ## customer state machine
#         state_machine = _sfn.StateMachine(self,
#                                           "CustomerDataAutomationPipline",
#                                           definition_body=_sfn.DefinitionBody.from_chainable(definition),
#                                           state_machine_name="Customer_data",
#                                           logs=_sfn.LogOptions(
#                                             destination=customer_log_group,
#                                             level=_sfn.LogLevel.ALL
#                                         ),
#                                           tracing_enabled=True
#                                           )
      
        
        
        
