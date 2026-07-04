USE superstore_analysis;

-- Q1: Orders with above-average sales

SELECT *
FROM orders
WHERE sales >
(
    SELECT AVG(sales)
    FROM orders
);

-- Q2: Highest order for every customer

SELECT
    customer_id,
    order_id,
    sales
FROM orders o
WHERE sales =
(
    SELECT MAX(sales)
    FROM orders
    WHERE customer_id = o.customer_id
);