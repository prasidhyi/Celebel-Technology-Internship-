USE shopease_db;

-- Q24: Classify products based on price

SELECT
    product_name,
    unit_price,
    CASE
        WHEN unit_price < 1000 THEN 'Budget'
        WHEN unit_price BETWEEN 1000 AND 3000 THEN 'Mid-Range'
        ELSE 'Premium'
    END AS price_tier
FROM products;

-- Q25: Count delivered and non-delivered orders

SELECT
    SUM(CASE WHEN status = 'Delivered' THEN 1 ELSE 0 END) AS delivered_orders,
    SUM(CASE WHEN status <> 'Delivered' THEN 1 ELSE 0 END) AS not_delivered_orders
FROM orders;

-- Q27: Transaction example

START TRANSACTION;

INSERT INTO orders
VALUES
(
1011,
102,
CURDATE(),
'Pending',
1598.00
);

INSERT INTO order_items
VALUES
(5016,1011,206,1,1299.00,0),
(5017,1011,208,1,299.00,0);

UPDATE products
SET stock_qty = stock_qty - 1
WHERE product_id = 206;

UPDATE products
SET stock_qty = stock_qty - 1
WHERE product_id = 208;

COMMIT;
