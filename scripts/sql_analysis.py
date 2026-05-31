import sqlite3
import pandas as pd

print("Create DB Connection")
connection = sqlite3.connect("data/relail_store.db")

print("\n Data Sheet")
data = pd.read_csv("data/cleaned_sales_data.csv")
print(data)

print("\n Store data into DB")
data.to_sql("sales", connection, if_exists="replace", index=False)

print("\n 1st SQL QUERY")
query = "Select * from Sales"
result = pd.read_sql(query,connection)
print(result)

print("\n Select Specific columns")
query = "Select Product, Revenue from Sales"
result = pd.read_sql(query,connection)
print(result)

print("\n Where clause")
query = """
Select * from Sales
where Category = 'Electronics'
"""
result = pd.read_sql(query,connection)
print(result)

print("\n Order By Clause")
query = """
Select Product, Revenue from Sales
Order by Revenue DESC
"""
result = pd.read_sql(query, connection)
print(result)

print("\n Group By Clause")
query = """
Select Category, Sum(Revenue) as Total_Revenue
from Sales
Group By Category
"""
result = pd.read_sql(query, connection)
print(result)

print("\n Average")
query = """
Select  Avg(Revenue) as AVERAGE_Revenue
from Sales
"""
result = pd.read_sql(query, connection)
print(result)

print("\n Find Top Product")
query = """
Select Product, Max(Revenue) as Top_Revenue
from Sales
Group By Product
"""
result = pd.read_sql(query, connection)
print(result)
query = """
Select Product, Revenue
from Sales
Order by Revenue DESC
LIMIT 1
"""
result = pd.read_sql(query, connection)
print(result)

connection.close()