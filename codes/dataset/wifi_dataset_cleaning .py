import pandas as pd

# Load dataset
df = pd.read_csv("wifi_dataset.csv")

print("Original Data:")
print(df.head())

# ---------------------------
# 1. Remove missing values
# ---------------------------
df.dropna(inplace=True)

# ---------------------------
# 2. Remove duplicates
# ---------------------------
df.drop_duplicates(inplace=True)

# ---------------------------
# 3. Fix data types
# ---------------------------
df["enrollment_no"] = df["enrollment_no"].astype(str)
df["devices_connected"] = df["devices_connected"].astype(int)
df["hours_used"] = df["hours_used"].astype(float)
df["data_usage_mb"] = df["data_usage_mb"].astype(float)

# ---------------------------
# 4. Remove invalid values
# ---------------------------

# Devices should be 1–5
df = df[(df["devices_connected"] >= 1) & (df["devices_connected"] <= 5)]

# Hours should be positive
df = df[df["hours_used"] > 0]

# Data usage should be positive
df = df[df["data_usage_mb"] > 0]

# ---------------------------
# 5. Standardize text columns
# ---------------------------
df["location"] = df["location"].str.strip().str.title()
df["time_slot"] = df["time_slot"].str.strip()

# ---------------------------
# 6. Reset index
# ---------------------------
df.reset_index(drop=True, inplace=True)

# ---------------------------
# 7. Save cleaned data
# ---------------------------
df.to_csv("wifi_cleaned_data.csv", index=False)

print("\n✅ Cleaned Data:")
print(df.head())

print("\n🎉 Cleaned CSV saved as wifi_student_usage_cleaned.csv")