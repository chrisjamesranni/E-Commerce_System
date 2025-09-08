
-- 1. Most valuable customer (highest total spend)
SELECT c.name AS customer_name, SUM(p.amount) AS total_spent
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
JOIN Payments p ON o.order_id = p.order_id
GROUP BY c.name
ORDER BY total_spent DESC
LIMIT 1;

-- 2. Category-wise sales summary
SELECT p.category, SUM(oi.quantity) AS total_units_sold, SUM(oi.quantity * oi.unit_price) AS total_sales
FROM Order_Items oi
JOIN Products p ON oi.product_id = p.product_id
GROUP BY p.category;

-- 3. Average order value per customer
SELECT c.name AS customer_name, AVG(oi.quantity * oi.unit_price) AS avg_order_value
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
JOIN Order_Items oi ON o.order_id = oi.order_id
GROUP BY c.name;

-- 4. Orders with multiple products
SELECT o.order_id, COUNT(oi.product_id) AS num_products
FROM Orders o
JOIN Order_Items oi ON o.order_id = oi.order_id
GROUP BY o.order_id
HAVING num_products > 1;

-- 5. Top 3 customers by order count
SELECT c.name AS customer_name, COUNT(o.order_id) AS orders_count
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
GROUP BY c.name
ORDER BY orders_count DESC
LIMIT 3;

-- 6. Revenue per product
SELECT p.name AS product_name, SUM(oi.quantity * oi.unit_price) AS revenue
FROM Products p
JOIN Order_Items oi ON p.product_id = oi.product_id
GROUP BY p.name
ORDER BY revenue DESC;

-- 7. Recent 5 orders with total amount
SELECT o.order_id, c.name AS customer_name, o.order_date, SUM(oi.quantity * oi.unit_price) AS total_amount
FROM Orders o
JOIN Customers c ON o.customer_id = c.customer_id
JOIN Order_Items oi ON o.order_id = oi.order_id
GROUP BY o.order_id, c.name, o.order_date
ORDER BY o.order_date DESC
LIMIT 5;

-- 8. Total revenue per payment method
SELECT method, SUM(amount) AS total_revenue
FROM Payments
GROUP BY method;
