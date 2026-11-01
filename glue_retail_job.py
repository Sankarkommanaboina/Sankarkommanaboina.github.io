# AWS Glue PySpark job
import sys
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.context import SparkContext
from pyspark.sql import functions as F, Window

args = getResolvedOptions(sys.argv, ["JOB_NAME","SOURCE_S3_PATH","TARGET_S3_PATH","QUARANTINE_S3_PATH"])
sc = SparkContext()
glue = GlueContext(sc)
spark = glue.spark_session
job = Job(glue)
job.init(args["JOB_NAME"], args)
df = (spark.read.option("header",True).option("inferSchema",True).csv(args["SOURCE_S3_PATH"])
      .withColumn("order_timestamp",F.to_timestamp("order_timestamp"))
      .withColumn("order_total",F.col("order_total").cast("double"))
      .withColumn("status",F.upper(F.trim("status"))))
valid = (F.col("event_id").isNotNull() & F.col("order_id").isNotNull()
         & F.col("order_timestamp").isNotNull() & F.col("order_total").isNotNull()
         & (F.col("order_total") >= 0)
         & F.col("status").isin("CREATED","PAID","SHIPPED","CANCELLED"))
w = Window.partitionBy("event_id").orderBy(F.col("order_timestamp").desc())
good = (df.filter(valid).withColumn("rn",F.row_number().over(w))
        .filter("rn=1").drop("rn").withColumn("order_date",F.to_date("order_timestamp")))
bad = df.filter(~valid)
good.write.mode("append").format("parquet").partitionBy("order_date").save(args["TARGET_S3_PATH"])
bad.write.mode("append").format("parquet").save(args["QUARANTINE_S3_PATH"])
job.commit()
