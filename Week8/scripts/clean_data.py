import pandas as pd
import re

orders = pd.read_csv("../data/orders.csv")
products = pd.read_csv("../data/products.csv")
customers = pd.read_csv("../data/customers.csv")
order_items = pd.read_csv("../data/order_items.csv")



def clean_orders(df):
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    df["customer_id"] = df["customer_id"].fillna(-1)

    return df


#
def clean_products(df):

    df["product_name"] = df["product_name"].str.strip().str.title()

    return df



def validate_emails(df):
    invalid_ids = []

    for index, row in df.iterrows():
        email = row["email"]

        if not re.match(r"[^@]+@[^@]+\.[^@]+", str(email)):
            invalid_ids.append(row["customer_id"])

    return invalid_ids



def check_referential_integrity(order_items, orders):
    valid_order_ids = set(orders["order_id"])

    invalid_rows = order_items[~order_items["order_id"].isin(valid_order_ids)]

    return invalid_rows



orders_clean = clean_orders(orders)
products_clean = clean_products(products)

invalid_emails = validate_emails(customers)
invalid_orders = check_referential_integrity(order_items, orders_clean)


orders_clean.to_csv("../data/clean_orders.csv", index=False)
products_clean.to_csv("../data/clean_products.csv", index=False)


print("Invalid Emails:", invalid_emails[:10])
print("Invalid Order References:")
print(invalid_orders.head())