## Sales Data Pipeline - End-to-End Data Engineering Project

## Objective

The objective of this project is to design and implement an end-to-end retail data engineering pipeline using a Medallion Architecture approach. The pipeline ingests raw transactional data from multiple source systems (CRM and ERP), processes it through multiple layers, and generates business-ready insights for analytics and reporting.

## Tools Used

Python
Pandas
CSV Files
Git & GitHub

## Architecture

The project follows a Medallion Architecture consisting of multiple layers:
Inbound → Raw → Landing → Bronze → Silver → Gold
Inbound Layer: Data ingestion from source systems
Raw Layer: Stores original data without modifications
Landing Layer: Structures data into a standardized format
Bronze Layer: Performs data cleaning and preprocessing
Silver Layer: Applies transformations, joins, and validations
Gold Layer: Generates business insights and aggregated data

## Data Sources
CRM System: Customer data
ERP System: Order and transaction data

The datasets include real-world inconsistencies such as missing values, duplicates, and invalid records to simulate production scenarios.

## Tasks Performed
Ingested data from CRM and ERP systems into the pipeline
Stored raw data for traceability
Structured data in the Landing layer
Performed data cleaning including:
Handling missing values
Removing duplicates
Fixing data types
Joined datasets to create a unified view
Validated data by removing invalid records
Created derived columns for business analysis
Generated KPIs such as:
Total Revenue
Revenue per Customer
Order Count
Customer Segmentation

## Project Structure
Sales-Data-Pipeline/
│
├── data/
│   ├── inbound/
│   ├── raw/
│   ├── landing/
│   ├── bronze/
│   ├── silver/
│   └── gold/
│
├── scripts/
│   ├── inbound_ingestion.py
│   ├── landing_processing.py
│   ├── bronze_processing.py
│   ├── silver_processing.py
│   └── gold_processing.py
│
└── README.md

## Key Features

End-to-end data pipeline implementation
Medallion Architecture design
Data cleaning and validation
Dataset integration using joins
Business logic implementation
KPI generation for analytics

## Future Enhancements

Implement Incremental Loading using High-Water Mark
Add Slowly Changing Dimensions (SCD Type 1 and Type 2)
Introduce Star Schema with fact and dimension tables
Migrate pipeline to PySpark and Databricks
Use Parquet format for optimized storage
Integrate with Power BI for dashboard visualization

## Conclusion
This project demonstrates a structured approach to building a scalable data engineering pipeline. It highlights key concepts such as data ingestion, transformation, validation, and analytics, and can be extended to production environments using cloud technologies.

 ## Author
Prasidhyi Kumar