import pandas as pd
import os

input_path = "../data/bronze/"
output_path = "../data/silver/"

os.makedirs(output_path, exist_ok=True)
customers = pd.read_csv(input_path + "crm_customers_bronze.csv")
orders = pd.read_csv(input_path + "erp_orders_bronze.csv")

merged_df = pd.merge(orders, customers, on="customer_id", how="left")

merged_df = merged_df.dropna(subset=["name"])

def categorize(amount):
    if amount > 50000:
        return "High Value"
    elif amount > 10000:
        return "Medium Value"
    else:
        return "Low Value"

merged_df["order_category"] = merged_df["amount"].apply(categorize)

merged_df.to_csv(output_path + "sales_silver.csv", index=False)

print("Silver layer processing completed successfully")