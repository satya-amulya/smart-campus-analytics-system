import pandas as pd

# 1. Load raw data
df = pd.read_csv('electricity.csv')

print("🔍 Initial shape:", df.shape)

# 2. Check missing values
print("\nMissing values:\n", df.isnull().sum())

# 3. Remove duplicates
df.drop_duplicates(inplace=True)

# 4. Fix data types
df['date'] = pd.to_datetime(df['date'])

# 5. Feature Engineering (simplified)
df['day_of_week'] = df['date'].dt.dayofweek
df['month'] = df['date'].dt.month

# 6. Validate numerical values
df['kwh'] = df['kwh'].clip(lower=0)

# 7. Sort data
df = df.sort_values(by=['date', 'area', 'hour'])

# 8. Save cleaned data
df.to_csv('electricity_clean.csv', index=False)

print("\n✅ Electricity cleaning complete!")
print("Final shape:", df.shape)
print(df.head())