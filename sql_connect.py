# import pandas as pd
# import mysql.connector

# # 1. Read CSV
# # df = pd.read_csv("F:\AI\python_project\sql_connect\sales.csv")

# # print("CSV read successfully!")
# # print(df)

# # 2. Connect to MySQL
# connection = mysql.connector.connect(
#     host="localhost",
#     port=3306,
#     user="root",
#     password="Suresh@143"
# )
# print("Connection object created")

# if connection.is_connected():
#     print("Connected to MySQL successfully!")

# # Later:
# # 3. Create table
# # 4. Insert data
# # 5. Commit
# # 6. Close connection

# connection.close()

# print("Connection closed.")

import pandas as pd
import mysql.connector

# Read CSV
df = pd.read_csv(r"F:\AI\python_project\sql_connect\sales.csv")

print("CSV loaded successfully!")
print(df)

# Connect to MySQL
connection = mysql.connector.MySQLConnection()

connection.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="Suresh@143",
    database="sales_db"
)

print("Connected to MySQL successfully!")

# cursor = connection.cursor()

# cursor.execute("CREATE DATABASE IF NOT EXISTS sales_db")

# print("Database created successfully!")

# cursor = connection.cursor()

# create_table_query = """
# CREATE TABLE IF NOT EXISTS sales (
#     order_id INT,
#     customer_id VARCHAR(20),
#     customer_name VARCHAR(100),
#     product VARCHAR(100),
#     category VARCHAR(50),
#     quantity INT,
#     price DECIMAL(10,2),
#     order_date DATE
# )
# """

# cursor.execute(create_table_query)

# print("Sales table created successfully!")
cursor = connection.cursor()
insert_query = """
INSERT INTO sales
(order_id, customer_id, customer_name, product, category,
 quantity, price, order_date)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""
for _, row in df.iterrows():
    cursor.execute(insert_query, tuple(row))

connection.commit()

# data = [tuple(row) for _, row in df.iterrows()]

# cursor.executemany(insert_query, data)

print("Data loaded successfully!")

cursor.close()
connection.close()