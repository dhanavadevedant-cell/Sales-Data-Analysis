import pandas as pd

df = pd.read_csv("sales_data.csv")

print(df.head())

print("Total Sales:", df["Sales"].sum())

print("Average Sales:", df["Sales"].mean())