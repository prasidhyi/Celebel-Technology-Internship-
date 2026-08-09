import pandas as pd
import random
from datetime import datetime, timedelta

def random_date():
    start = datetime(2023, 1, 1)
    end = datetime(2024, 12, 31)
    delta = end - start
    random_days = random.randint(0, delta.days)
    date = start + timedelta(days=random_days)

    if random.random() < 0.1:
        return date.strftime("%d-%m-%Y %H:%M:%S")
    return date.strftime("%Y-%m-%d %H:%M:%S")


def random_email(name):
    domains = ["gmail.com", "yahoo.com", "outlook.com"]

    if random.random() < 0.02:
        return name + "gmail.com"   

    return name + "@" + random.choice(domains)


# -------------------------------
# 1. Customers
# -------------------------------
customers = []
for i in range(1, 501):
    name = f"customer_{i}"
    customers.append([
        i,
        name,
        random_email(name),
        random_date(),
        random.choice(["REGULAR", "PREMIUM", "VIP"])
    ])

customers_df = pd.DataFrame(customers, columns=[
    "customer_id", "customer_name", "email",
    "registration_date", "customer_type"
])

customers_df.to_csv("../data/customers.csv", index=False)


# -------------------------------
# 2. Products
# -------------------------------
categories = ["Electronics", "Clothing", "Home", "Books"]

products = []
for i in range(1, 501):
    name = f" product_{i} "  
    products.append([
        i,
        name,
        random.choice(categories),
        "subcategory_" + str(random.randint(1, 5)),
        random.randint(100, 2000)
    ])

products_df = pd.DataFrame(products, columns=[
    "product_id", "product_name", "category",
    "subcategory", "cost_price"
])

products_df.to_csv("../data/products.csv", index=False)


# -------------------------------
# 3. Orders
# -------------------------------
orders = []
for i in range(1, 501):

    # 5% NULL customer_id
    if random.random() < 0.05:
        customer_id = None
    else:
        customer_id = random.randint(1, 500)

    orders.append([
        i,
        customer_id,
        random_date(),
        random.choice(["PLACED", "SHIPPED", "DELIVERED", "CANCELLED", "RETURNED"]),
        random.choice(["NORTH", "SOUTH", "EAST", "WEST"])
    ])

orders_df = pd.DataFrame(orders, columns=[
    "order_id", "customer_id", "order_date",
    "status", "region_code"
])

orders_df.to_csv("../data/orders.csv", index=False)



# -------------------------------
# 4. Order Items
# -------------------------------
order_items = []
for i in range(1, 1001):

    quantity = random.randint(1, 5)

    if random.random() < 0.03:
        quantity = -quantity

    order_items.append([
        i,
        random.randint(1, 550), 
        random.randint(1, 500),
        quantity,
        random.randint(100, 2000),
        random.randint(0, 50)
    ])

order_items_df = pd.DataFrame(order_items, columns=[
    "item_id", "order_id", "product_id",
    "quantity", "unit_price", "discount_percent"
])

order_items_df.to_csv("../data/order_items.csv", index=False)

print("CSV files generated successfully!")