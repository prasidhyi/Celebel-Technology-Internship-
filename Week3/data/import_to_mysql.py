import pandas as pd
import pymysql

# Read the cleaned CSV
df = pd.read_csv("Superstore_Clean.csv")

# Connect to MySQL
connection = pymysql.connect(
    host="localhost",
    user="pythonuser",
password="python123",
    database="superstore_analysis"
)

cursor = connection.cursor()

# Insert data row by row
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO superstore_raw (
            row_id, order_id, order_date, ship_date, ship_mode,
            customer_id, customer_name, segment, country, city,
            state, postal_code, region, product_id, category,
            sub_category, product_name, sales, quantity,
            discount, profit
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s, %s, %s, %s,
                %s, %s)
    """, tuple(row))

connection.commit()

print(f"{len(df)} rows inserted successfully!")

cursor.close()
connection.close()