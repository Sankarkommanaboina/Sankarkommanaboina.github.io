Multi-Cloud Data Engineering Portfolio
Hands-on data engineering projects demonstrating end-to-end pipeline patterns across Microsoft Azure, Amazon Web Services (AWS), and Google Cloud Platform (GCP). All included datasets are synthetic.
Projects at a glance
Cloud	Project	Use case	Technologies
Azure	Healthcare Claims Lakehouse	Ingest, clean, and analyze claims data	ADLS, Azure Databricks, PySpark, Azure Synapse Analytics
AWS	Retail Event Data Platform	Validate and process retail events	Amazon S3, AWS Lambda, AWS Glue, PySpark, Amazon Athena
GCP	Mobility Data Streaming Pipeline	Process mobility events for analytics	Pub/Sub, Apache Beam, Dataflow, BigQuery


1. Azure — Healthcare Claims Lakehouse
Scenario: A healthcare analytics team receives claims files from multiple sources and needs to standardize records, apply quality checks, and prepare trusted datasets for reporting.

Architecture:
Synthetic Claims CSV
  -> Azure Data Lake Storage (Raw)
  -> Azure Databricks / PySpark
       - schema validation
       - cleansing and standardization
       - curated transformations
  -> ADLS (Curated)
  -> Azure Synapse Analytics
  -> Reporting / Analytics
Project capabilities
- Batch ingestion and a raw-to-curated lakehouse pattern.
- PySpark transformations for claims data.
- Basic data-quality checks and standardized output.
- SQL examples for analytical querying in Synapse.
Project files: The Azure project folder contains the sample dataset, local transformation, Databricks job, Synapse SQL, and project-specific documentation.
2. AWS — Retail Event Data Platform
Scenario: A retail business receives order and transaction events from multiple channels. The platform validates incoming records, processes them, and exposes curated data for analytics.

Architecture:
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
Project capabilities
- Object-storage-based data lake organization.
- Event validation with an AWS Lambda example.
- Batch transformation using AWS Glue and PySpark.
- SQL-based analysis using Athena.
Project files: The AWS project folder contains sample data, local transformation, Lambda validator, Glue job, Athena SQL, and project-specific documentation.
3. GCP — Mobility Data Streaming Pipeline
Scenario: A mobility platform generates continuous trip and location events. The pipeline processes incoming events and writes analytics-ready records to a warehouse.

Architecture:
Mobility Event Producer
  -> Google Cloud Pub/Sub
  -> Apache Beam / Dataflow
       - parse events
       - validate records
       - transform event fields
  -> BigQuery
  -> Analytics / Dashboards
Project capabilities
- Streaming pipeline concepts and event-driven ingestion.
- Apache Beam transformations suitable for Dataflow.
- Validation and transformation of mobility events.
- BigQuery SQL for analytical queries.
Project files: The GCP project folder contains sample data, local transformation, Beam/Dataflow pipeline, BigQuery SQL, and project-specific documentation.
Shared engineering practices
- Layered data organization: separate incoming/raw data from curated analytical data.
- Data quality: validate required fields, schemas, and record values.
- Distributed processing: use PySpark or Apache Beam transformation patterns.
- SQL analytics: publish data for querying and reporting.
- Reproducibility: include synthetic input data and code examples.
- Cloud-native design: use each provider's storage, processing, and analytics services.
Running the local examples
The repository includes local Python transformations so you can explore the data flow without provisioning cloud resources.
1. Clone the repository.
2. Create and activate a Python virtual environment.
3. Install dependencies from requirements.txt, where applicable.
4. Open the project folder you want to explore.
5. Follow that project's README and run its local transformation.
git clone <your-repository-url>
cd <repository-folder>
python -m venv .venv

# Windows
.venv\\Scripts\\activate

# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
Cloud-native examples require the relevant cloud account, permissions, service configuration, and resource names. Configure these before deployment. Never commit credentials, access keys, service-account files, or secrets to GitHub.
Disclaimer
All sample records are synthetic. These are demonstration projects. Cloud deployment steps may require adjustments for service versions, account configuration, IAM roles, networking, and billing. Review cloud costs and permissions before provisioning resources.
