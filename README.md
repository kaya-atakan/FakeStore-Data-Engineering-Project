# FakeStore-Data-Engineering-Project
Data Pipeline Orchestration and Transformation

This project implements a robust data pipeline orchestrated through Apache Airflow, facilitating the seamless flow of data from the Fakestore API to Google Cloud Storage and onwards to a PostgreSQL data warehouse. Leveraging Airbyte, an open-source data integration engine, this pipeline effortlessly connects data sources to destinations. The pipeline's architecture enables the retrieval of data from the Fakestore API, storing it in a staging zone within a Google Cloud Storage Bucket. This staged data serves as the foundation for the Extract-Load (EL) phase, which Airbyte streamlines with its intuitive interface.

Post-loading, data transformation occurs directly within the PostgreSQL data warehouse, courtesy of dbt. This eliminates the need to extract data from the warehouse for transformation purposes, streamlining and optimizing the entire process. The workflow is designed to ensure efficient data handling and transformation without unnecessary movement, enhancing overall pipeline performance.

Tools and Environment Used:

VS Code
Apache Airflow
Airbyte
Docker Desktop
PostgreSQL Database
Gmail account
Google Cloud Account
Google Cloud Storage Bucket
Virtualization and WSL enabled (if using Windows PC)

This repository serves as a comprehensive guide and resource for setting up the environment, understanding the data pipeline architecture, and orchestrating data transformations using industry-standard tools. Dive into the provided documentation and resources to seamlessly replicate and adapt this powerful data pipeline for your specific use case.

This project wouldn't exist today if such an inspirational article hadn't come into play:

https://medium.com/@chibuokejuliet/modern-data-stack-airbyte-dbt-and-apache-airflow-5339c72e3296
