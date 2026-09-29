import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = pd.read_csv("sales.csv")

X = data[["temperature_c"]]
y = data["ice_creams_sold"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
)

model = LinearRegression()
model.fit(X_train, y_train)

slope = model.coef_[0]
intercept = model.intercept_

print("Training complete.")
print("Learned slope:", slope)
print("Learned intercept:", intercept)

example_temperature = 26
estimated_sales = slope * example_temperature + intercept

print("\nTemperature in Celsius:", example_temperature)
print("Sales estimated using the learned formula:", estimated_sales)