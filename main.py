import pandas as pd

data = pd.read_csv("sales.csv")

X = data[["temperature_c"]]
y = data["ice_creams_sold"]

print("INPUT: TEMPERATURE")
print(X.head())

print("\nTARGET: SALES")
print(y.head())

print("\nINPUT SHAPE")
print(X.shape)

print("\nTARGET SHAPE")
print(y.shape)