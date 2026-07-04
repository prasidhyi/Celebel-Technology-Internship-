-- Top 5 Customers

WITH customer_sales AS (
    SELECT
        customer_id,
        SUM(sales) AS total_sales
    FROM orders
    GROUP BY customer_id
)

SELECT
    customer_id,
    total_sales
FROM customer_sales
ORDER BY total_sales DESC
LIMIT 5;

-- Bottom 5 Customers

WITH customer_sales AS (
    SELECT
        customer_id,
        SUM(sales) AS total_sales
    FROM orders
    GROUP BY customer_id
)

SELECT
    customer_id,
    total_sales
FROM customer_sales
ORDER BY total_sales
LIMIT 5;
-- Customers with only one order

SELECT
    customer_id,
    COUNT(order_id) AS total_orders
FROM orders
GROUP BY customer_id
HAVING COUNT(order_id) = 1;
-- Above average customers

WITH customer_sales AS (
    SELECT
        customer_id,
        SUM(sales) AS total_sales
    FROM orders
    GROUP BY customer_id
)

SELECT *
FROM customer_sales
WHERE total_sales >
(
    SELECT AVG(total_sales)
    FROM customer_sales
);
-- Highest order value per customer

SELECT
    customer_id,
    MAX(sales) AS highest_order
FROM orders
GROUP BY customer_id;