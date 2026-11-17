
import pandas as pd

df = pd.read_csv("data/train.csv")

print("Shape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

print("\nNumeric Summary:")
print(df.describe())

print("\nUnique Values:")
print(df.nunique())

print(df["spoilage_pct"].describe())
print(df["power_cuts_hours"].describe())
print(df["crop"].value_counts())
print(df["chamber"].value_counts())

print("\nCrop Raw Values:")
for x in df["crop"].unique():
    print(repr(x), df["crop"].value_counts().get(x))

print("\nSpoilage Above 100:")
print(df[df["spoilage_pct"] > 100][
    ["record_id", "crop", "spoilage_pct"]
])

print("\nTop 10 Power Cuts:")
print(df.nlargest(10, "power_cuts_hours")[
    ["record_id", "date", "storage_days", "power_cuts_hours"]
])

print("\nSpoilage Found at Unloading:")
print(df["spoilage_found_at_unloading"].describe())
print(df["spoilage_found_at_unloading"].value_counts().head(10))


df["max_possible_hours"] = df["storage_days"] * 24

print(df[df["power_cuts_hours"] > df["max_possible_hours"]][
    ["record_id", "storage_days", "power_cuts_hours", "max_possible_hours"]
])

print("Invalid power cut records:",
      (df["power_cuts_hours"] > df["max_possible_hours"]).sum())

