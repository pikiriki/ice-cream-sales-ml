import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv("sales.csv")

X = data[["temperature_c"]]
y = data["ice_creams_sold"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
)

print("TRAINING INPUT SHAPE")
print(X_train.shape)

print("\nTRAINING TARGET SHAPE")
print(y_train.shape)

print("\nTEST INPUT SHAPE")
print(X_test.shape)

print("\nTEST TARGET SHAPE")
print(y_test.shape)