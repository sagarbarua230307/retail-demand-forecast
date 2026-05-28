import pandas as pd

data = pd.read_csv("data/sales_data.csv")

print(data)
print(data.columns)
print(data["Product"])

data["Revenue"] = data["Price"] * data["Quantity"]
print(data)

total_revenue = data["Revenue"].sum()
print("Total Revenue: ", total_revenue)

highest_revenue = data["Revenue"].max()
print("Highest Revenue: ", highest_revenue)

electronics = data[data["Category"] == "Electronics"]
print(electronics)

sorted_data = data.sort_values(by="Revenue", ascending=False)
print(sorted_data)

print("Average Revenue: ",data["Revenue"].mean())

data.to_csv("data/updated_sales_data.csv", index=False)
