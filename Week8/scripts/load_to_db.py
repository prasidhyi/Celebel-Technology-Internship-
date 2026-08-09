import sqlite3
import pandas as pd

conn = sqlite3.connect("../data/ecommerce.db")
pd.read_csv("../data/clean_orders.csv").to_sql("orders", conn, if_exists="replace", index=False)
pd.read_csv("../data/clean_products.csv").to_sql("products", conn, if_exists="replace", index=False)
pd.read_csv("../data/customers.csv").to_sql("customers", conn, if_exists="replace", index=False)
pd.read_csv("../data/order_items.csv").to_sql("order_items", conn, if_exists="replace", index=False)

conn.close()

print("Data loaded into SQLite!")