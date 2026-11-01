import json, os, uuid
from datetime import datetime, timezone
import boto3

s3 = boto3.client("s3")
BUCKET = os.environ["RAW_BUCKET"]
PREFIX = os.environ.get("RAW_PREFIX","raw/orders")

def lambda_handler(event, context):
    records = event.get("Records", [])
    payloads = [json.loads(r["body"]) for r in records] if records else [event]
    saved = []
    for item in payloads:
        required = ["event_id","order_id","order_timestamp","status","order_total"]
        missing = [k for k in required if item.get(k) in (None,"")]
        if missing: raise ValueError(f"Missing fields: {missing}")
        if float(item["order_total"]) < 0: raise ValueError("Negative order_total")
        now = datetime.now(timezone.utc)
        key = f"{PREFIX}/ingest_date={now:%Y-%m-%d}/{item['event_id']}-{uuid.uuid4().hex}.json"
        s3.put_object(Bucket=BUCKET, Key=key, Body=json.dumps(item).encode(), ContentType="application/json")
        saved.append({"event_id":item["event_id"],"key":key})
    return {"statusCode":200,"body":json.dumps({"saved":saved})}
