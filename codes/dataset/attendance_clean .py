import pandas as pd

# 🔹 STEP 1: Load raw dataset
df = pd.read_csv("attendance.csv")

print("Original Shape:", df.shape)

# 🔹 STEP 2: Standardize column names (safety)
df.columns = df.columns.str.strip().str.lower()

# 🔹 STEP 3: Convert date column
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# 🔹 STEP 4: Remove missing values
df = df.dropna()

# 🔹 STEP 5: Remove duplicates
df = df.drop_duplicates()

# 🔹 STEP 6: Ensure present column is valid (0 or 1 only)
df = df[df['present'].isin([0, 1])]

# 🔹 STEP 7: Fix string formatting (important for grouping later)
df['student_name'] = df['student_name'].str.strip()
df['branch'] = df['branch'].str.upper().str.strip()
df['course'] = df['course'].str.strip()
df['year_semester'] = df['year_semester'].astype(str).str.strip()

# 🔹 STEP 8: Add useful feature (helps analysis)
df['day'] = df['date'].dt.day_name()

# 🔹 STEP 9: Final check
print("Cleaned Shape:", df.shape)
print("\nMissing values:\n", df.isnull().sum())

# 🔹 STEP 10: Save cleaned dataset
df.to_csv("attendance_cleaned.csv", index=False)

print("\n✅ Attendance cleaned and saved as attendance_cleaned.csv")