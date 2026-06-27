USE shopease_db;

-- Q7: Display all delivered orders

SELECT *
FROM orders
WHERE status = 'Delivered';

-- Q8: Electronics products above ₹2000

SELECT *
FROM products
WHERE category = 'Electronics'
AND unit_price > 2000;

-- Q9: Customers from Maharashtra who joined in 2024

SELECT *
FROM customers
WHERE state = 'Maharashtra'
AND join_date BETWEEN '2024-01-01' AND '2024-12-31';

-- Q10: Orders between two dates except cancelled

SELECT *
FROM orders
WHERE order_date BETWEEN '2024-08-10' AND '2024-08-25'
AND status <> 'Cancelled';

