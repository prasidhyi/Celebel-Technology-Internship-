# Week 7 - Delta Lake Incremental Data Processing

## Objective

The objective of this assignment is to perform incremental data processing using Delta Lake by loading customer data, cleaning the dataset, applying MERGE operations to update existing records and insert new records, validating the results, and displaying the final Delta table.

## Tools Used

- Python
- Apache Spark
- PySpark
- Delta Lake
- Jupyter Notebook
- Git & GitHub

## Tasks Performed

- Loaded customer master data into a Delta table.
- Removed duplicate records and handled missing values.
- Loaded incremental customer data.
- Performed MERGE operations to update existing records and insert new records.
- Validated the final dataset using row count and duplicate checks.
- Displayed the final Delta table.

## Project Structure

```
Week7/
│
├── data/
│   ├── customer_master.csv
│   ├── customer_incremental.csv
│   └── customer_delta/
│
├── notebooks/
│   └── Week7_Delta_Lake.ipynb
│
├── outputs/
│
├── README.md
├── INSIGHTS.md
└── requirements.txt
```

## Author

Prasidhyi Kumar