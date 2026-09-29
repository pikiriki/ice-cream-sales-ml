import pandas as pd

data = pd.read_csv("sales.csv")

print("FIRST FIVE OBSERVATIONS")
print(data.head())

print("\nCOLUMN NAMES")
print(data.columns.tolist())

print("\nNUMBER OF OBSERVATIONS")
print(len(data))

print("\nMISSING VALUES PER COLUMN")
print(data.isna().sum())

print("\nTEMPERATURE RANGE")
print("Minimum:", data["temperature_c"].min())
print("Maximum:", data["temperature_c"].max())