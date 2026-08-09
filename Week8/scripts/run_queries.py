import sqlite3

conn = sqlite3.connect("../data/ecommerce.db")
cursor = conn.cursor()


query1 = """
SELECT 
    p.category,
    SUM(oi.quantity * oi.unit_price * (1 - oi.discount_percent / 100.0)) AS total_revenue
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
GROUP BY p.category;
"""

print("---- Revenue per Category ----")
cursor.execute(query1)
for row in cursor.fetchall():
    print(row)

query2 = """
SELECT 
    o.customer_id,
    SUM(oi.quantity * oi.unit_price * (1 - oi.discount_percent / 100.0)) AS total_spent
FROM orders o
JOIN order_items oi ON o.order_id = oi.order_id
GROUP BY o.customer_id
ORDER BY total_spent DESC
LIMIT 10;
"""

print("\n---- Top 10 Customers ----")
cursor.execute(query2)
for row in cursor.fetchall():
    print(row)



query3 = """
SELECT 
    strftime('%Y-%m', order_date) AS month,
    COUNT(*) AS order_count
FROM orders
GROUP BY month
ORDER BY month;
"""

print("\n---- Monthly Orders ----")
cursor.execute(query3)
for row in cursor.fetchall():
    print(row)


conn.close()