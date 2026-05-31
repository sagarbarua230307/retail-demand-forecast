import pandas as pd
data = pd.read_csv("data/cleaned_sales_data.csv")
data["Revenue"] = data["Price"] * data["Quantity"]
print(data)

print(data.info())
print(data.describe())
total_revenue = data["Revenue"].sum()
print("Total Revenue:", total_revenue)
print("\n ------ Business Insights -------")
print("\n 1. Total Revenue:", total_revenue)
print("\n 2. Average Revenue: ", data["Revenue"].mean())
print("\n 3. Highest Revenue :" + data.loc[data["Revenue"].idxmax()]["Product"])
print("\n 4. Lowest Revenue :" + data.loc[data["Revenue"].idxmin()]["Product"])

with open("reports/eda_report.txt", "w") as file:
    file.write("------ EDA Report -------\n")
    file.write(f"Total Revenue: {total_revenue}\n")
    file.write(f"Average Revenue: {data['Revenue'].mean()}\n")
    file.write(f"Highest Revenue Product: {data.loc[data['Revenue'].idxmax()]['Product']}\n")
    file.write(f"Lowest Revenue Product: {data.loc[data['Revenue'].idxmin()]['Product']}\n")                                                                                                                                                 