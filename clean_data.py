
import pandas as pd

df = pd.read_csv("data/train.csv")

df["crop"] = df["crop"].str.strip().str.lower()

mp = {
    "app.": "apple",
    "pot.": "potato",
    "oni.": "onion"
}

df["crop"] = df["crop"].replace(mp)

df["date"] = pd.to_datetime(df["date"])

cols = ["storage_days", "temp_set_c", "humidity_pct",
        "power_cuts_hours", "bag_weight_kg",
        "door_openings_per_day", "spoilage_found_at_unloading",
        "spoilage_pct"]

for c in cols:
    df[c] = pd.to_numeric(df[c], errors="coerce")

print("Shape:", df.shape)
print("\nCrop Values:")
print(df["crop"].value_counts())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

sp = df[df["spoilage_pct"] > 100]
print("\nSpoilage Above 100:", len(sp))

pc = df[df["power_cuts_hours"] > df["storage_days"] * 24]
print("Invalid Power Cut Records:", len(pc))

df.to_csv("data/train_clean.csv", index=False)

sp.to_csv("data/spoilage_review.csv", index=False)
pc.to_csv("data/power_cut_review.csv", index=False)

print("\nCleaned dataset saved successfully!")

print("\nFinal Crop Categories:")
print(df["crop"].value_counts())

print("\nUnique Crops:")
print(df["crop"].unique())


print("\nSpoilage Records Above 100:")
print(df[df["spoilage_pct"] > 100][
    ["record_id", "crop", "spoilage_pct"]
])
df["max_possible_hours"] = df["storage_days"] * 24

print("\nInvalid Power Cut Records:")
print(df[df["power_cuts_hours"] > df["max_possible_hours"]][
    ["record_id", "storage_days", "power_cuts_hours", "max_possible_hours"]
])