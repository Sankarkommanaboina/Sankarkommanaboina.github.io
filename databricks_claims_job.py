# Run in Azure Databricks. Configure these as job widgets/parameters.
from pyspark.sql import functions as F, Window

for name in ["SOURCE_PATH", "SILVER_PATH", "GOLD_PATH", "QUARANTINE_PATH"]:
    dbutils.widgets.text(name, "")
p = {n: dbutils.widgets.get(n) for n in ["SOURCE_PATH","SILVER_PATH","GOLD_PATH","QUARANTINE_PATH"]}
if not all(p.values()):
    raise ValueError("All four path parameters are required")

df = (spark.read.option("header", True).csv(p["SOURCE_PATH"])
      .withColumn("service_date", F.to_date("service_date"))
      .withColumn("source_updated_at", F.to_timestamp("source_updated_at"))
      .withColumn("paid_amount", F.col("paid_amount").cast("double"))
      .withColumn("claim_status", F.upper(F.trim("claim_status"))))
reason = F.concat_ws("|",
    F.when(F.col("claim_id").isNull() | (F.trim("claim_id") == ""), "MISSING_CLAIM_ID"),
    F.when(F.col("member_id").isNull() | (F.trim("member_id") == ""), "MISSING_MEMBER_ID"),
    F.when(F.col("service_date").isNull(), "INVALID_SERVICE_DATE"),
    F.when(F.col("paid_amount").isNull() | (F.col("paid_amount") < 0), "INVALID_PAID_AMOUNT"),
    F.when(~F.col("claim_status").isin("PAID","DENIED","PENDING"), "INVALID_STATUS"))
checked = df.withColumn("reject_reason", reason)
good, bad = checked.filter("reject_reason = ''"), checked.filter("reject_reason != ''")
w = Window.partitionBy("claim_id").orderBy(F.col("source_updated_at").desc_nulls_last())
silver = (good.withColumn("rn", F.row_number().over(w)).filter("rn=1")
          .drop("rn","reject_reason").withColumn("service_month", F.date_format("service_date","yyyy-MM")))
silver.write.format("delta").mode("append").partitionBy("service_month").save(p["SILVER_PATH"])
bad.write.format("delta").mode("append").save(p["QUARANTINE_PATH"])
(silver.filter("claim_status='PAID'").groupBy("service_date")
 .agg(F.countDistinct("claim_id").alias("claim_count"), F.sum("paid_amount").alias("paid_amount_total"))
 .write.format("delta").mode("overwrite").save(p["GOLD_PATH"]))
