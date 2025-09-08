# 🛒 E-Commerce Sales & Inventory Management (SQL Project)

## 📌 Overview

This project simulates a real-world **E-commerce system** built using **MySQL Workbench**.

It manages **customers, products, orders, payments, and inventory**, and provides **business insights** through SQL queries.

Designed as a **portfolio project**, it showcases database design, SQL querying, and reporting skills—similar to internal data systems used by companies.

---

## 🛠️ Tech Stack

- **Database:** MySQL
- **Tool:** MySQL Workbench
- **Language:** SQL (DDL, DML, Queries)

---

## 🗂️ Database Design

### Entities (Tables)

- **Customers** – Stores customer information.
- **Products** – Catalog of products with prices and stock levels.
- **Orders** – Records of customer purchases.
- **Order\_Items** – Details of products in each order.
- **Payments** – Payment transactions linked to orders.

### Relationships

- A **customer** can place multiple orders.
- An **order** can include multiple products.
- Each **order** has one payment.
- **Products** are linked to orders through order items.

*See the ****\`\`**** for a visual representation.*

---

## 🔑 Features

- Track **customers, products, orders, and payments**.
- Monitor **inventory levels** and detect low stock.
- Analyze **monthly revenue** and **best-selling products**.
- Identify **most valuable customers** based on total spending.

---

## 📜 Repository Files

| File                   | Description                                         |
| ---------------------- | --------------------------------------------------- |
| `fakedata`             | python script to create multiple insert commands    |
| `01_create_tables.sql` | Script to create the database schema                |
| `02_insert_data.sql`   | Inserts sample data for testing                     |
| `03_queries.sql`       | Business queries and reports                        |
| `ER_Diagram.png`       | Entity-Relationship Diagram of the database         |
| `README.md`            | Project documentation                               |

---

## 🚀 How to Run

1. **Open MySQL Workbench** and connect to your database.
2. Create a schema:

```sql
CREATE DATABASE ecommerce_db;
USE ecommerce_db;
```

3. Run `01_create_tables.sql` to create the tables.
4. Run `02_insert_data.sql` to insert sample data.
5. Execute queries from `03_queries.sql` to generate business insights.

---

## 📈 Future Enhancements

- Create **dashboards** for real-time analytics.
- Implement **automatic inventory alerts**.
- Add **customer segmentation analysis**.
- Develop **REST APIs** to integrate with a web front-end.

