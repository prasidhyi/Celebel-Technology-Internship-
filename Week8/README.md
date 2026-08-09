Week 8 - E-Commerce Order Analytics System

Objective
The objective of this assignment is to design and develop an end-to-end data analytics system for an e-commerce platform using Python and SQL. The task involves generating realistic datasets with inconsistencies, performing data cleaning and validation, ensuring referential integrity, executing analytical SQL queries, and building a command-line reporting tool to generate business insights.

Tools Used
Python
Pandas
SQLite
SQL
VS Code
Git & GitHub

Tasks Performed
Generated synthetic datasets for orders, order_items, products, and customers with intentional inconsistencies such as null values, invalid emails, incorrect date formats, and negative quantities.
Performed data cleaning using Pandas by handling missing values, fixing date formats, and normalizing product names.
Implemented email validation using regular expressions.
Ensured referential integrity by identifying mismatched foreign keys between order_items and orders tables.
Loaded cleaned datasets into a SQLite database.
Executed SQL queries including joins, aggregations, filtering, and grouping to derive business insights.
Applied advanced SQL concepts such as window functions (running totals, ranking, and lag operations).
Developed a command-line reporting tool to generate summaries including total orders, revenue, unique customers, and top products based on user input.
Handled edge cases such as invalid references, incorrect discount values, and inconsistent data entries.

Project Structure
week8-ecommerce-project/
│
├── data/
│   ├── customers.csv
│   ├── products.csv
│   ├── orders.csv
│   ├── order_items.csv
│   ├── clean_orders.csv
│   ├── clean_products.csv
│   └── ecommerce.db
│
├── scripts/
│   ├── generate_data.py
│   ├── clean_data.py
│   ├── load_to_db.py
│   └── run_queries.py
│
├── sql/
│   └── analysis.sql
│
├── reports/
│
├── main.py
└── README.md

Author
Prasidhyi Kumar