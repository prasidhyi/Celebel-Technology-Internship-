USE shopease_db;

-- Q13: Total number of orders

SELECT COUNT(*) AS total_orders
FROM orders;

-- Q14: Total revenue from delivered orders

SELECT SUM(total_amount) AS total_revenue
FROM orders
WHERE status = 'Delivered';

-- Q15: Average price by category

SELECT
    category,
    AVG(unit_price) AS average_price
FROM products
GROUP BY category;

-- Q16: Orders and revenue by status

SELECT
    status,
    COUNT(order_id) AS total_orders,
    SUM(total_amount) AS total_revenue
FROM orders
GROUP BY status
ORDER BY total_revenue DESC;

-- Q17: Highest and lowest priced products

SELECT
    category,
    MAX(unit_price) AS highest_price,
    MIN(unit_price) AS lowest_price
FROM products
GROUP BY category;

-- Q18: Categories with average price greater than ₹2000

SELECT
    category,
    AVG(unit_price) AS average_price
FROM products
GROUP BY category
HAVING AVG(unit_price) > 2000;