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

example_temperature = 26

new_day = pd.DataFrame({
    "temperature_c": [example_temperature]
})

predictions = model.predict(new_day)
predicted_sales = predictions[0]

formula_sales = slope * example_temperature + intercept

print("Temperature in Celsius:", example_temperature)
print("Predicted ice-cream sales:", predicted_sales)
print("Estimate from the learned formula:", formula_sales)