# Week 4 Summary

This assignment focused on understanding Azure cloud services and implementing a simple data pipeline using Azure Data Factory.

A Resource Group and Storage Account were created in Microsoft Azure. A Blob Container was configured, and the Superstore CSV dataset was uploaded successfully.

Azure Data Factory was then created to build an end-to-end data pipeline. A Linked Service was configured to connect ADF with Azure Blob Storage. Source and destination datasets were created, followed by the implementation of a pipeline using Get Metadata and Copy Data activities.

The pipeline was executed successfully, and Azure Monitor confirmed that all activities completed successfully. IAM permissions were configured to allow Azure Data Factory to access the Storage Account securely.