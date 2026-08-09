import pandas as pd
import os

input_path = "../data/raw/"
output_path = "../data/landing/"

os.makedirs(output_path, exist_ok=True)
crm_df = pd.read_csv(input_path + "crm_customers_raw.csv")
erp_df = pd.read_csv(input_path + "erp_orders_raw.csv")

crm_df.to_csv(output_path + "crm_customers_landing.csv", index=False)
erp_df.to_csv(output_path + "erp_orders_landing.csv", index=False)

print("Landing layer completed")