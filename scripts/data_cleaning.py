import pandas as pd

data = pd.read_csv("data/dirty_sales_data.csv")
print(data)
#Detect Missing Values
print(data.isnull())
#Count Missing Cells
print(data.isnull().sum())
#Remove missing values
cleaned_data = data.dropna()
print(cleaned_data)
#Remove duplicate rows
print(data.duplicated())
data= data.drop_duplicates()
print(data)
#Handle Wrong Datatypes
data["Price"] = pd.to_numeric(data["Price"], errors="coerce")
print(data)
#Remove Null Values
data = data.dropna()
print(data)
#Check Datatype
print(data.dtypes)
#Revenue Column
data["Revenue"] = data["Price"] * data["Quantity"]
print(data)
#GEnerate Cleaning Summary
print("Total Clean Rows: ", len(data))
#save data clean sheet
data.to_csv("data/cleaned_sales_data.csv", index=False)
