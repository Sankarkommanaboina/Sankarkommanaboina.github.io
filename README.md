# Multi-Cloud Data Engineering Portfolio

Hands-on portfolio projects demonstrating end-to-end data engineering patterns across **Microsoft Azure, AWS, and Google Cloud Platform (GCP)**. All included datasets are synthetic.

> These are personal learning and demonstration projects, not production systems or client work.

## Projects at a glance

| Cloud | Project | Use case | Technologies |
|---|---|---|---|
| Azure | Healthcare Claims Lakehouse | Ingest, clean, and analyze claims data | ADLS, Azure Databricks, PySpark, Azure Synapse Analytics |
| AWS | Retail Event Data Platform | Validate and process retail events | Amazon S3, AWS Lambda, AWS Glue, PySpark, Amazon Athena |
| GCP | Mobility Data Streaming Pipeline | Process mobility events for analytics | Pub/Sub, Apache Beam, Dataflow, BigQuery |

---

## 1. Azure — Healthcare Claims Lakehouse

**Scenario:** A healthcare analytics team receives claims files from multiple sources and needs to standardize records, apply quality checks, and prepare trusted datasets for reporting.

**Architecture:**
```text
Synthetic Claims CSV
  -> Azure Data Lake Storage (Raw)
  -> Azure Databricks / PySpark
       - schema validation
       - cleansing and standardization
       - curated transformations
  -> ADLS (Curated)
  -> Azure Synapse Analytics
  -> Reporting / Analytics
```

**What it demonstrates**
- Batch ingestion and a raw-to-curated lakehouse pattern.
- PySpark transformations for claims data.
- Basic data-quality checks and standardized output.
- SQL examples for analytical querying in Synapse.

**Repository contents:** See the Azure project folder for the sample dataset, local transformation, Databricks job, Synapse SQL, and project-specific README.

---

## 2. AWS — Retail Event Data Platform

**Scenario:** A retail business receives order and transaction events from multiple channels. The platform validates incoming records, processes them, and exposes curated data for analytics.

**Architecture:**
```text
Retail Event Data
  -> Amazon S3 (Landing)
  -> AWS Lambda (event validation)
  -> AWS Glue / PySpark
       - transformation
       - normalization
       - curated output
  -> Amazon S3 (Curated)
  -> Amazon Athena
  -> Analytics / Reporting
```

**What it demonstrates**
- Object-storage-based data lake organization.
- Event validation with an AWS Lambda example.
- Batch transformation using AWS Glue and PySpark.
- SQL-based analysis using Athena.

**Repository contents:** See the AWS project folder for sample data, local transformation, Lambda validator, Glue job, Athena SQL, and project-specific README.

---

## 3. GCP — Mobility Data Streaming Pipeline

**Scenario:** A mobility platform generates continuous trip and location events. The pipeline processes incoming events and writes analytics-ready records to a warehouse.

**Architecture:**
```text
Mobility Event Producer
  -> Google Cloud Pub/Sub
  -> Apache Beam / Dataflow
       - parse events
       - validate records
       - transform event fields
  -> BigQuery
  -> Analytics / Dashboards
```

**What it demonstrates**
- Streaming pipeline concepts and event-driven ingestion.
- Apache Beam transformations suitable for Dataflow.
- Validation and transformation of mobility events.
- BigQuery SQL for analytical queries.

**Repository contents:** See the GCP project folder for sample data, local transformation, Beam/Dataflow pipeline, BigQuery SQL, and project-specific README.

---

## Shared engineering practices

- **Layered data organization:** separate incoming/raw data from curated analytical data.
- **Data quality:** validate required fields, schemas, and record values.
- **Distributed processing:** use PySpark or Apache Beam transformation patterns.
- **SQL analytics:** publish data for querying and reporting.
- **Reproducibility:** include synthetic input data and code examples.
- **Cloud-native design:** use each provider's storage, processing, and analytics services.

## Running the local examples

The repository includes local Python transformations so you can explore the data flow without provisioning cloud resources.

1. Clone the repository.
2. Create and activate a Python virtual environment.
3. Install dependencies from `requirements.txt`, where applicable.
4. Open the project folder you want to explore.
5. Follow that project's README and run its local transformation.

```bash
git clone <your-repository-url>
cd <repository-folder>
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
```

Cloud-native examples require the relevant cloud account, permissions, service configuration, and resource names. Configure these before deployment. Never commit credentials, access keys, service-account files, or secrets to GitHub.

## Suggested GitHub repository description

Multi-cloud data engineering portfolio featuring Azure Databricks and Synapse, AWS S3/Lambda/Glue/Athena, and GCP Pub/Sub/Dataflow/BigQuery, with synthetic datasets and end-to-end pipeline examples.

## Resume and interview positioning

Describe this repository as a **personal hands-on portfolio** demonstrating multi-cloud data engineering concepts. Be ready to explain the architecture, transformation logic, data-quality checks, SQL, and which components were run locally versus deployed to cloud services.

## Disclaimer

All sample records are synthetic. Cloud deployment steps may require adjustments for service versions, account configuration, IAM roles, networking, and billing. Review cloud costs and permissions before provisioning resources.
