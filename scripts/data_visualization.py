import pandas as pd
import matplotlib.pyplot as plt
#Read cleaned dataset
data = pd.read_csv("data/cleaned_sales_data.csv")
#create revenue column
data["Revenue"] = data["Price"] * data["Quantity"]
print(data)

#Bar Chart
plt.bar(data["Product"], data["Revenue"])
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.show()

#Line Chart
plt.plot(data["Product"], data["Revenue"])
plt.title("Revenue Trends")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.show()

#Pie Chart
category_sales = data.groupby("Category")["Revenue"].sum()
plt.pie(category_sales, labels=category_sales.index, autopct='%1.1f%%')
plt.title("Category Revenue Share")
plt.show()

#Histogram
plt.hist(data["Revenue"])
plt.title("Revenue Distribution")
plt.xlabel("Revenue")
plt.ylabel("Frequency")
plt.show()

#Save charts
plt.bar(data["Product"], data["Revenue"])
plt.title("Product Revenue")
plt.savefig("reports/revenue_chart.png")

#Business Insights
top_product = data.loc[data["Revenue"].idxmax()]
print("Top Product: ")
print(top_product)

#Average Revenue Analysis
average_revenue = data["Revenue"].mean()
print("Average Revenue: ", average_revenue)