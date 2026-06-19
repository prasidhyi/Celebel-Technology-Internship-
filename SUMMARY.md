# Summary — Shopping Dataset Cleaning

## What was done

The raw dataset (`data/raw/shopping_dataset.csv`) contained **260 rows and 9 columns**
of shopping order data (order ID, customer name, product, category, price, quantity,
order date, payment method, region).

### Exploration
- Checked shape, column names, data types, and summary statistics.
- `price` and `quantity` were numeric; the rest were categorical/text.

### Missing values
| Column | Missing values | Strategy |
|---|---|---|
| `category` | 12 | Filled with `"Unknown"` |
| `payment_method` | 9 | Filled with `"Unknown"` |
| `price` | 6 | Filled with column median |
| `quantity` | 4 | Filled with column median |

Numeric columns were filled with the **median** (more robust to outliers than the mean).
Categorical columns were filled with an explicit `"Unknown"` placeholder rather than a
guessed value, since there's no defensible way to infer a missing category or payment
method from the other fields.

### Duplicates
**10 exact duplicate rows** were found and removed, keeping the first occurrence of each.

### Derived column
Added `total_amount = price * quantity` to represent the value of each order line.

### Output
The cleaned dataset — **250 rows, 10 columns**, zero missing values, zero duplicates —
was saved to `data/cleaned/shopping_dataset_cleaned.csv`.

## Before → After

| | Raw | Cleaned |
|---|---|---|
| Rows | 260 | 250 |
| Columns | 9 | 10 (added `total_amount`) |
| Missing values | 31 cells | 0 |
| Duplicate rows | 10 | 0 |

## Notes

This run used a synthetic sample dataset (see `README.md` for why, and how to swap in
the real Kaggle dataset). The cleaning logic itself — identify missing values, fill
numerically with median / categorically with a placeholder, drop exact duplicates,
derive `total_amount` — applies the same way regardless of which underlying CSV is used.
