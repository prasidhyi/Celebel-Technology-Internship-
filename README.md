# Shopping Dataset — Pandas Data Exploration & Cleaning

A beginner-level Python/Pandas exercise: load a shopping/e-commerce dataset, explore it,
clean it, and export the cleaned result.

## Objective

Learn Python basics and perform basic data exploration and cleaning using Pandas.

## Repo structure

```
shopping-data-cleaning/
├── data/
│   ├── raw/
│   │   └── shopping_dataset.csv          # input data
│   └── cleaned/
│       └── shopping_dataset_cleaned.csv  # output of the notebook
├── notebooks/
│   └── data_cleaning.ipynb               # main notebook (all steps)
├── SUMMARY.md                            # brief write-up of findings/approach
└── README.md
```

## About the dataset

This repo ships with a **synthetic sample dataset** (`data/raw/shopping_dataset.csv`)
modeled on the structure of the
[Kaggle "Shopping Dataset" by anvitkumar](https://www.kaggle.com/datasets/anvitkumar/shopping-dataset) —
order-level e-commerce data with product, price, quantity, category, and customer info.
It includes intentionally injected missing values and duplicate rows so the cleaning
steps in the notebook have real issues to fix.

**To use the actual Kaggle data:**
1. Download the CSV from Kaggle (requires a free Kaggle account).
2. Replace `data/raw/shopping_dataset.csv` with the downloaded file (same filename, or
   update the `RAW_PATH` variable in the notebook's Step 1 cell).
3. If column names differ from `price` / `quantity`, update the `PRICE_COL` / `QTY_COL`
   variables in the notebook's Step 6 cell.
4. Re-run all cells (`Kernel → Restart & Run All` in Jupyter, or `jupyter nbconvert --execute`).

## Steps performed in the notebook

1. Load the CSV into a Pandas DataFrame
2. Explore the data (`head`, `tail`, `shape`, `columns`, `dtypes`, `describe`, `info`)
3. Identify and handle missing values (median fill for numeric columns, `"Unknown"` for categorical)
4. Basic operations — filter rows, select columns
5. Remove duplicate rows
6. Create a derived column: `total_amount = price * quantity`
7. Save the cleaned dataset to `data/cleaned/shopping_dataset_cleaned.csv`

## How to run

```bash
pip install pandas numpy jupyter
jupyter notebook notebooks/data_cleaning.ipynb
```

Then run all cells from top to bottom.

## Tech

- Python 3
- pandas
- numpy
