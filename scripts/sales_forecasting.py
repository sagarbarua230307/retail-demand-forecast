import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
data = pd.read_csv("data/monthly_sales.csv")
print(data)
x = data[["Month"]]
y= data[["Revenue"]]
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42)
model =LinearRegression()
model.fit(x_train, y_train)
predictions = model.predict(x_test)
print(predictions)

future_month = [[13],[14],[15],[20]]
future_prediction = model.predict(future_month)
print("Predicted Revenue For Month 13,14,15,20:")
print(future_prediction)

score = model.score(x_test,y_test)
print("Model Accuracy: ",score)

print("Slope: ",model.coef_)
print("Intercept: ",model.intercept_)

with open("reports/forecast_report.txt","w") as file:
    file.write(
        f"Predicted Revenue Month 13: {future_prediction[0]}\n"
    )
    file.write(
        f"Predicted Revenue Month 14: {future_prediction[1]}\n"
    )
    file.write(
        f"Predicted Revenue Month 15: {future_prediction[2]}\n"
    )
    file.write(
        f"Predicted Revenue Month 20: {future_prediction[3]}\n"
    )