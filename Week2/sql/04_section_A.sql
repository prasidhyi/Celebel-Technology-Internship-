USE shopease_db;

-- Q1: Display all customer records
SELECT *
FROM customers;

-- Q2: Show customer names and city
SELECT first_name,
       last_name,
       city
FROM customers;

-- Q3: Unique product categories
SELECT DISTINCT category
FROM products;