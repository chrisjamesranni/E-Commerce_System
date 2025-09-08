import random
from faker import Faker
import os

fake = Faker()

# ---------------------------
# Ensure file goes in the same folder as the script
# ---------------------------
base_dir = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(base_dir, "02_insert_data.sql")

print("Script located in:", base_dir)
print("Output file will be:", output_file)

# ---------------------------
# 1. Customers
# ---------------------------
customers = []
for cid in range(1, 1001):
    name = fake.name().replace("'", "''")
    email = fake.unique.email().replace("'", "''")
    phone = fake.phone_number().replace("'", "''")
    city = fake.city().replace("'", "''")
    join_date = fake.date_between(start_date="-5y", end_date="today")
    customers.append(
        f"INSERT INTO Customers (customer_id, name, email, phone, city, join_date) "
        f"VALUES ({cid}, '{name}', '{email}', '{phone}', '{city}', '{join_date}');"
    )

# ---------------------------
# 2. Products
# ---------------------------
categories = ["Electronics", "Clothing", "Books", "Toys", "Home", "Sports"]
products = []
for pid in range(1, 1001):
    name = (fake.word().capitalize() + " " + fake.word().capitalize()).replace("'", "''")
    category = random.choice(categories)
    price = round(random.uniform(5, 500), 2)
    stock_quantity = random.randint(10, 500)
    products.append(
        f"INSERT INTO Products (product_id, name, category, price, stock_quantity) "
        f"VALUES ({pid}, '{name}', '{category}', {price}, {stock_quantity});"
    )

# ---------------------------
# 3. Orders
# ---------------------------
statuses = ["Pending", "Shipped", "Delivered", "Cancelled"]
orders = []
for oid in range(1, 1001):
    customer_id = random.randint(1, 1000)
    order_date = fake.date_between(start_date="-2y", end_date="today")
    status = random.choice(statuses)
    orders.append(
        f"INSERT INTO Orders (order_id, customer_id, order_date, status) "
        f"VALUES ({oid}, {customer_id}, '{order_date}', '{status}');"
    )

# ---------------------------
# 4. Order_Items
# ---------------------------
order_items = []
order_item_id = 1
for oid in range(1, 1001):
    for _ in range(random.randint(1, 5)):
        product_id = random.randint(1, 1000)
        quantity = random.randint(1, 3)
        unit_price = round(random.uniform(5, 500), 2)
        order_items.append(
            f"INSERT INTO Order_Items (order_item_id, order_id, product_id, quantity, unit_price) "
            f"VALUES ({order_item_id}, {oid}, {product_id}, {quantity}, {unit_price});"
        )
        order_item_id += 1

# ---------------------------
# 5. Payments
# ---------------------------
methods = ["Credit Card", "PayPal", "Bank Transfer", "Cash"]
payments = []
payment_id = 1
for oid in range(1, 1001):
    if random.random() < 0.8:  # ~80% of orders are paid
        amount = round(random.uniform(20, 2000), 2)
        payment_date = fake.date_between(start_date="-2y", end_date="today")
        method = random.choice(methods)
        payments.append(
            f"INSERT INTO Payments (payment_id, order_id, amount, payment_date, method) "
            f"VALUES ({payment_id}, {oid}, {amount}, '{payment_date}', '{method}');"
        )
        payment_id += 1

# ---------------------------
# Write to SQL file in script's folder
# ---------------------------
with open(output_file, "w", encoding="utf-8") as f:
    f.write("-- Insert Customers\n")
    f.write("\n".join(customers) + "\n\n")

    f.write("-- Insert Products\n")
    f.write("\n".join(products) + "\n\n")

    f.write("-- Insert Orders\n")
    f.write("\n".join(orders) + "\n\n")

    f.write("-- Insert Order_Items\n")
    f.write("\n".join(order_items) + "\n\n")

    f.write("-- Insert Payments\n")
    f.write("\n".join(payments) + "\n\n")

print(f"✅ SQL insert commands generated in: {output_file}")
