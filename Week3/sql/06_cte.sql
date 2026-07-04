USE superstore_analysis;
-- Q3: Total sales for each customer

WITH customer_sales AS (
    SELECT
        customer_id,
        SUM(sales) AS total_sales
    FROM orders
    GROUP BY customer_id
)

SELECT *
FROM customer_sales
ORDER BY total_sales DESC;
-- Q4: Customers with above-average total sales

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