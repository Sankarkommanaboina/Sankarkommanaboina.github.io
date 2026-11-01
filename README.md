# Cloud Data Engineering + RAG Portfolio

A practical, interview-ready portfolio covering **Azure, AWS, Google Cloud, and a cross-cloud RAG solution**.

## Projects

1. **Azure — Healthcare claims lakehouse:** ADLS Gen2 → Azure Data Factory → Databricks → Delta Lake → Synapse serverless SQL / Power BI.
2. **AWS — Retail event-driven data platform:** S3 → EventBridge/SQS → Glue → Lambda → Athena/Redshift, with data quality and monitoring.
3. **GCP — Mobility analytics platform:** Cloud Storage → Pub/Sub → Dataflow → BigQuery → Looker.
4. **RAG — Enterprise data engineering knowledge assistant:** ingest project documents, chunk and embed them, retrieve relevant context, and generate grounded answers with citations.

Each case study includes a business scenario, architecture, data flow, implementation plan, sample code/SQL, validation, security, monitoring, and interview talking points.

## Quick start

Requirements: Python 3.10+, `pandas`, `python-dotenv`. Cloud SDKs and services are optional until you deploy.

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
python src/transform_claims.py
python src/transform_retail_orders.py
python src/transform_mobility.py
```

The sample scripts run locally against the included CSV files and write curated outputs to `output/`.
They are intentionally cloud-neutral transformations; the case studies explain how to connect them to each cloud's managed services.

## Suggested portfolio presentation

- Put this repository on GitHub after reviewing and customizing it.
- Add your own architecture diagrams and screenshots from a sandbox deployment.
- Clearly describe this as a **portfolio implementation / hands-on project**, not production client work unless you actually deployed it for a client.
- Replace sample metrics with measurements from your own run. Do not claim the illustrative business outcomes as measured results.

## Repository map

- `docs/` — detailed case studies and interview walkthroughs
- `src/` — runnable local ETL examples
- `data/` — synthetic sample datasets
- `sql/` — warehouse transformation examples
- `cloud_templates/` — deployment outlines and starter configuration
