import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

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

baseline_sales = y_train.mean()
baseline_predictions = [baseline_sales] * len(X_test)

test_predictions = model.predict(X_test)

model_mae = mean_absolute_error(y_test, test_predictions)
baseline_mae = mean_absolute_error(y_test, baseline_predictions)

results = pd.DataFrame({
    "actual_sales": y_test,
    "predicted_sales": test_predictions,
    "absolute_error": abs(y_test - test_predictions),
})

print("Baseline prediction for every test example:", baseline_sales)
print("Model test MAE:", model_mae)
print("Baseline test MAE:", baseline_mae)

print("\nTEST RESULTS")
print(results.round(2).to_string(index=False))

print("\nDataset temperature range in Celsius:")
print("Minimum:", data["temperature_c"].min())
print("Maximum:", data["temperature_c"].max())
print("Predictions outside this range may be unreliable.")

temperature_text = input("\nEnter a temperature in Celsius: ")
temperature = float(temperature_text)

new_day = pd.DataFrame({
    "temperature_c": [temperature]
})

predictions = model.predict(new_day)
predicted_sales = predictions[0]

print("Temperature in Celsius:", temperature)
print("Predicted ice-cream sales:", predicted_sales)