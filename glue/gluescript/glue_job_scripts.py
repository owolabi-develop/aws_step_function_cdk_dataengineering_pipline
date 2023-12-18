import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)


CustomerDataCatalog = glueContext.create_dynamic_frame.from_catalog(
    database="customer-database",
    table_name="olist_customers_dataset_csv",
    transformation_ctx="CustomerDataCatalog",
)

# Change Schema
CustomerChangeSchema= ApplyMapping.apply(
    frame=CustomerDataCatalog,
    mappings=[
        ("customer_id", "string", "customer_id", "string"),
        ("customer_unique_id", "string", "customer_unique_id", "string"),
        ("customer_zip_code", "int", "customer_zip_code", "int"),
        ("customer_city", "string", "customer_city", "string"),
        ("customer_state", "string", "customer_state", "string"),
        ("partition_0", "string", "partition_0", "string")
    ],
    transformation_ctx="CustomerChangeSchema",
)

## write data to s3 consumption bucket and partition by "state", "street", "status"

ConsumptionAmazonS3 = glueContext.write_dynamic_frame.from_options(
    frame=CustomerChangeSchema,
    connection_type="s3",
    format="glueparquet",
    connection_options={
        "path": "s3://consumptions-customer-bucket",
        "partitionKeys": ["customer_state"],
    },
    format_options={"compression": "snappy"},
    transformation_ctx="ConsumptionAmazonS3",
)

job.commit()
