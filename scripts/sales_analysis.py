product = ["Laptop", "Mouse", "Keyboard", "Monitor"]
prices = [50000, 2000, 3000, 15000]
sales = [40, 30, 15, 23]

def calculate_revenue(price, quantity):
    return price * quantity
total_company_revenue =0
for i in range(len(product)):
    revenue = calculate_revenue(prices[i], sales[i])
    print("Product: ", product[i])
    print("Revenue: ", revenue)
    print("-------------")
    total_company_revenue += revenue
    print("Total Company Revenue: ", total_company_revenue)
    print("-------------")
