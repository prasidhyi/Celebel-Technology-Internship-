## Q4

Primary Keys:

- customers → customer_id
- products → product_id
- orders → order_id
- order_items → item_id

A Primary Key uniquely identifies every record in a table. It cannot contain duplicate values or NULL values, ensuring that every row can be referenced uniquely.

## Q5

The email column has two constraints:

- UNIQUE
- NOT NULL

UNIQUE ensures that no two customers can have the same email address.

NOT NULL ensures that every customer must provide an email.

If we try to insert another customer with an existing email, MySQL will return a Duplicate Entry error.

## Q6

The INSERT statement fails because the unit_price column has a CHECK constraint.

CHECK(unit_price > 0)

Since -50 is not greater than 0, MySQL rejects the record and displays an error.

## Q11

The `idx_orders_date` index is created on the `order_date` column of the `orders` table.

It helps MySQL find records based on the order date without scanning every row in the table. This improves query performance, especially when the table contains a large number of records.

Example query:

```sql
SELECT *
FROM orders
WHERE order_date = '2024-08-15';
```

This query can make use of the `idx_orders_date` index to retrieve matching records more efficiently.

## Q12

No, the index is generally not used efficiently because the `YEAR()` function is applied to the `join_date` column. MySQL has to calculate the year for every row before filtering.

A better approach is to filter using a date range:

```sql
SELECT *
FROM customers
WHERE join_date BETWEEN '2024-01-01' AND '2024-12-31';
```

This query is SARGable (Search Argument Able), allowing MySQL to use an index on the `join_date` column more effectively.

## Q22

### LEFT JOIN

A LEFT JOIN returns all records from the left table and the matching records from the right table. If there is no matching record, NULL values are returned for the columns of the right table.

Example:

```sql
SELECT c.customer_id, c.first_name, o.order_id
FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id;
```

### RIGHT JOIN

A RIGHT JOIN returns all records from the right table and the matching records from the left table.

Example:

```sql
SELECT c.customer_id, o.order_id
FROM customers c
RIGHT JOIN orders o
ON c.customer_id = o.customer_id;
```

### FULL OUTER JOIN

A FULL OUTER JOIN returns all matching records from both tables. If there is no match, NULL values are returned for the missing side. It is useful when we want every record from both tables, regardless of whether a match exists.

## Q23

### Foreign Keys

1. `orders.customer_id` → `customers.customer_id`

2. `order_items.order_id` → `orders.order_id`

3. `order_items.product_id` → `products.product_id`

These foreign keys maintain referential integrity between the tables. If we try to insert an order with `customer_id = 999`, MySQL will reject the record because no customer with that ID exists in the `customers` table. A foreign key constraint error will be generated.

## Q26

### ACID Properties
Atomicity (A)
A transaction is completed entirely or not at all. If any step fails, the entire transaction is rolled back.
Consistency (C)
A transaction keeps the database in a valid state by following all rules and constraints.
Isolation (I)
Multiple transactions can run at the same time without affecting each other's results.
Durability (D)
Once a transaction is committed, the changes are permanently stored even if the system crashes.

### Example: Bank Transfer

Suppose ₹500 is transferred from Account A to Account B.

Atomicity: Both debit and credit should happen together. If one fails, both are cancelled.
Consistency: The total amount of money remains the same before and after the transaction.
Isolation: Two transfers happening simultaneously do not interfere with each other.
Durability:Once the transfer is successful, the updated balance is permanently saved.
