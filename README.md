# Cloud Data Engineering & RAG Projects

This repository contains my hands-on work and personal projects across **Azure, AWS, Google Cloud, Data Engineering, and Generative AI (RAG)**.

The projects focus on building practical data pipelines, processing structured and streaming data, working with cloud data platforms, and exploring how AI and LLMs can be integrated with enterprise data.

## Projects

1. **Azure – Healthcare Data Engineering:** Building a healthcare claims data pipeline using ADLS Gen2, Azure Data Factory, Databricks, Delta Lake, and Synapse Analytics.

2. **AWS – Retail Data Engineering:** Developing an event-driven data processing workflow using Amazon S3, AWS Glue, Lambda, EventBridge, SQS, Athena, and Redshift.

3. **GCP – Mobility Data Analytics:** Working with streaming data pipelines using Google Cloud Storage, Pub/Sub, Dataflow, BigQuery, and Looker.

4. **RAG – Data Engineering Knowledge Assistant:** Exploring Retrieval-Augmented Generation (RAG) to process technical documents, generate embeddings, retrieve relevant information, and provide context-based responses using LLMs.

## Technologies & Tools

- **Cloud:** Microsoft Azure, AWS, Google Cloud Platform
- **Data Engineering:** Python, SQL, PySpark, ETL/ELT, Data Pipelines
- **Azure:** ADF, ADLS Gen2, Databricks, Delta Lake, Synapse Analytics
- **AWS:** S3, Glue, Lambda, Athena, Redshift, EventBridge
- **GCP:** BigQuery, Pub/Sub, Dataflow, Cloud Storage
- **AI & GenAI:** RAG, LLMs, Embeddings, Vector Search, Document Processing

## Getting Started

The repository includes sample datasets, Python scripts, SQL queries, and project documentation.

To run the local examples:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

python src/transform_claims.py
python src/transform_retail_orders.py
python src/transform_mobility.py
```

The examples use sample datasets and can be extended to work with cloud services.

## Repository Structure

- `docs/` – Project documentation and technical details
- `src/` – Python data processing scripts
- `data/` – Sample datasets
- `sql/` – SQL queries and transformations
- `cloud_templates/` – Cloud deployment notes and configurations

I use these projects to explore different cloud technologies, improve my data engineering skills, and experiment with practical applications of AI and RAG.
