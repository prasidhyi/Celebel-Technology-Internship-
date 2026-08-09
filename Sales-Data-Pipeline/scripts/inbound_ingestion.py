import pandas as pd
import os

input_path = "../data/inbound/"
output_path = "../data/raw/"

os.makedirs(output_path, exist_ok=True)


crm_df = pd.read_csv(input_path + "crm_customers.csv")
erp_df = pd.read_csv(input_path + "erp_orders.csv")

crm_df.to_csv(output_path + "crm_customers_raw.csv", index=False)
erp_df.to_csv(output_path + "erp_orders_raw.csv", index=False)

print("Inbound data successfully moved to Raw layer")