USE superstore_analysis;

-- Insert Customers
INSERT INTO customers (
    customer_id,
    customer_name,
    segment,
    country,
    city,
    state,
    postal_code,
    region
)
SELECT DISTINCT
    customer_id,
    customer_name,
    segment,
    country,
    city,
    state,
    postal_code,
    region
FROM superstore_raw;


-- Insert Products
INSERT INTO products (
    product_id,
    category,
    sub_category,
    product_name
)
SELECT DISTINCT
    product_id,
    category,
    sub_category,
    product_name
FROM superstore_raw;


-- Insert Orders
INSERT INTO orders (
    order_id,
    order_date,
    ship_date,
    ship_mode,
    customer_id,
    sales,
    quantity,
    discount,
    profit
)
SELECT DISTINCT
    order_id,
    order_date,
    ship_date,
    ship_mode,
    customer_id,
    sales,
    quantity,
    discount,
    profit
FROM superstore_raw;
