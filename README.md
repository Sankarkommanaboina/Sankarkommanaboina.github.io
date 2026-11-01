# GCP mobility streaming analytics

Flow: mobile/vehicle events -> Pub/Sub -> Apache Beam/Dataflow -> BigQuery -> Looker.

Run `python gcp/transform_local.py` locally. `mobility_dataflow.py` is the streaming Beam example. Deploy with DataflowRunner and pass `--input_subscription`, `--output_table`, `--deadletter_table`, project, region and staging/temp bucket arguments. Create BigQuery dataset/table and grant the worker service account required Pub/Sub, BigQuery and bucket permissions. Review event-time/watermark behavior before production use.
