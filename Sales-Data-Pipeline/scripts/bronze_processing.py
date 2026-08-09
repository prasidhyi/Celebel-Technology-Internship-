import pandas as pd
import os

input_path = "../data/landing/"
output_path = "../data/bronze/"

os.makedirs(output_path, exist_ok=True)

crm_df = pd.read_csv(input_path + "crm_customers_landing.csv")
erp_df = pd.read_csv(input_path + "erp_orders_landing.csv")

crm_df = crm_df.drop_duplicates()

crm_df['email'] = crm_df['email'].fillna("unknown@gmail.com")

crm_df['name'] = crm_df['name'].str.strip()

erp_df = erp_df.drop_duplicates()
erp_df['amount'] = erp_df['amount'].fillna(0)

erp_df['amount'] = erp_df['amount'].astype(float)

crm_df.to_csv(output_path + "crm_customers_bronze.csv", index=False)
erp_df.to_csv(output_path + "erp_orders_bronze.csv", index=False)

print("Bronze layer processing completed successfully")