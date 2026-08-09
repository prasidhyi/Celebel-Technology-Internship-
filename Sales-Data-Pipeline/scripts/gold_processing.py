import pandas as pd
import os
input_path = "../data/silver/"
output_path = "../data/gold/"

os.makedirs(output_path, exist_ok=True)
df = pd.read_csv(input_path + "sales_silver.csv")

total_revenue = df["amount"].sum()
revenue_per_customer = df.groupby("customer_id")["amount"].sum().reset_index()

order_count = df.groupby("customer_id")["order_id"].count().reset_index()
order_count.rename(columns={"order_id": "total_orders"}, inplace=True)
customer_segment = df.groupby("customer_id")["amount"].sum().reset_index()

def segment(amount):
    if amount > 50000:
        return "Premium"
    elif amount > 20000:
        return "Regular"
    else:
        return "Basic"

customer_segment["segment"] = customer_segment["amount"].apply(segment)
revenue_per_customer.to_csv(output_path + "revenue_per_customer.csv", index=False)
order_count.to_csv(output_path + "order_count.csv", index=False)
customer_segment.to_csv(output_path + "customer_segment.csv", index=False)
with open(output_path + "total_revenue.txt", "w") as f:
    f.write(f"Total Revenue: {total_revenue}")

print("Gold layer processing completed successfully")