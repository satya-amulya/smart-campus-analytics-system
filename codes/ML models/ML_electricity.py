import pandas as pd
import numpy as np

# ML MODEL TO FORECAST ELECTRICITY USAGE

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df = pd.read_csv('data/data_files/electricity_clean.csv')

print("Columns:", df.columns)


df = pd.get_dummies(df, columns=['area'])

X = df.drop(['kwh', 'date'], axis=1)
y = df['kwh']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestRegressor()
model.fit(X_train, y_train)

pred = model.predict(X_test)

print("\nMODEL PERFORMANCE")

print("MAE:", mean_absolute_error(y_test, pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, pred)))
print("R2 Score:", r2_score(y_test, pred))
print("\n Sample Predictions vs Actual:")

for i in range(5):
    print(f"Predicted: {pred[i]:.2f} | Actual: {y_test.iloc[i]:.2f}")

#PLOTS

import matplotlib.pyplot as plt

plt.figure()

plt.scatter(y_test, pred)
plt.xlabel("Actual kWh")
plt.ylabel("Predicted kWh")
plt.title("Actual vs Predicted Electricity Consumption")

plt.show()

#LINE COMPLARISION ACTUAL VS PREDICTED PLOT

plt.figure()

plt.plot(y_test.values[:50], label="Actual")
plt.plot(pred[:50], label="Predicted")

plt.legend()
plt.title("Actual vs Predicted (First 50 Samples)")

plt.show()

#ERROR PLOT

errors = y_test - pred

plt.figure()

plt.hist(errors, bins=20)
plt.title("Prediction Error Distribution")

plt.xlabel("Error")
plt.ylabel("Frequency")

plt.show()


 # INPUT DATA FOR FORECASTING DATA

print("\n🔮 Electricity Forecast (User Input)")

hour = int(input("Enter hour (0–23): "))
day = int(input("Enter day_of_week (0=Mon, 6=Sun): "))
month = int(input("Enter month (1–12): "))
area = input("Enter area (A1, A2, ..., C6, Common Area): ")

input_dict = {col: 0 for col in X.columns}

input_dict['hour'] = hour
input_dict['day_of_week'] = day
input_dict['month'] = month

# set selected area = 1
area_col = f"area_{area}"
if area_col in input_dict:
    input_dict[area_col] = 1
else:
    print("Invalid area!")

# convert to dataframe
input_df = pd.DataFrame([input_dict])

# predict
prediction = model.predict(input_df)

print(f"\n Predicted Electricity Usage: {prediction[0]:.2f} kWh")