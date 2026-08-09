import sqlite3


conn = sqlite3.connect("data/ecommerce.db")
cursor = conn.cursor()

report_type = input("Enter report type (daily/monthly): ")
start_date = input("Enter start date (YYYY-MM-DD): ")
end_date = input("Enter end date (YYYY-MM-DD): ")


query_orders = f"""
SELECT COUNT(*) 
FROM orders
WHERE date(order_date) BETWEEN '{start_date}' AND '{end_date}';
"""

cursor.execute(query_orders)
total_orders = cursor.fetchone()[0]

query_revenue = f"""
SELECT SUM(oi.quantity * oi.unit_price * (1 - oi.discount_percent / 100.0))
FROM orders o
JOIN order_items oi ON o.order_id = oi.order_id
WHERE date(o.order_date) BETWEEN '{start_date}' AND '{end_date}';
"""

cursor.execute(query_revenue)
revenue = cursor.fetchone()[0]

query_customers = f"""
SELECT COUNT(DISTINCT customer_id)
FROM orders
WHERE date(order_date) BETWEEN '{start_date}' AND '{end_date}';
"""

cursor.execute(query_customers)
customers = cursor.fetchone()[0]


query_top_products = f"""
SELECT p.product_name,
       SUM(oi.quantity) as total_qty
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
JOIN orders o ON o.order_id = oi.order_id
WHERE date(o.order_date) BETWEEN '{start_date}' AND '{end_date}'
GROUP BY p.product_name
ORDER BY total_qty DESC
LIMIT 3;
"""

cursor.execute(query_top_products)
top_products = cursor.fetchall()


print("\n📊 REPORT")
print("Total Orders:", total_orders)
print("Total Revenue:", revenue)
print("Unique Customers:", customers)

print("\nTop 3 Products:")
for p in top_products:
    print(p)

conn.close()