USE superstore_analysis;

-- Q5: Rank customers by total sales

WITH customer_sales AS (
    SELECT
        customer_id,
        SUM(sales) AS total_sales
    FROM orders
    GROUP BY customer_id
)

SELECT
    customer_id,
    total_sales,
    RANK() OVER (ORDER BY total_sales DESC) AS customer_rank
FROM customer_sales;

-- Q6: Row number for each customer's orders

SELECT
    customer_id,
    order_id,
    order_date,
    sales,
    ROW_NUMBER() OVER (
        PARTITION BY customer_id
        ORDER BY order_date
    ) AS order_number
FROM orders;

-- Q7: Top 3 customers

WITH customer_sales AS (
    SELECT
        customer_id,
        SUM(sales) AS total_sales
    FROM orders
    GROUP BY customer_id
)

SELECT *
FROM (
    SELECT
        customer_id,
        total_sales,
        RANK() OVER (ORDER BY total_sales DESC) AS customer_rank
    FROM customer_sales
) ranked_customers
WHERE customer_rank <= 3;