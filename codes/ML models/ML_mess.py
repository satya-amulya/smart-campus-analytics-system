import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ML MODEL TO PREDICT PEAK MESS HOURS

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


df = pd.read_csv('data/data_files/mess_clean.csv')

print("Columns:", df.columns)

df = pd.get_dummies(df, columns=['meal'])

X = df[['hour', 'minute', 'day_of_week', 'month'] + 
       [col for col in df.columns if col.startswith('meal_')]]

y = df['headcount']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestRegressor(n_estimators=200)
model.fit(X_train, y_train)

pred = model.predict(X_test)

print("\n MODEL PERFORMANCE")

print("MAE:", mean_absolute_error(y_test, pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, pred)))
print("R2 Score:", r2_score(y_test, pred))

#PLOTS

plt.figure()
plt.scatter(y_test, pred)
plt.xlabel("Actual Headcount")
plt.ylabel("Predicted Headcount")
plt.title("Actual vs Predicted Mess Crowd")
plt.show()

# PEAK HOUR PREDICTION

print("\n PEAK HOUR ANALYSIS (PER MEAL)\n")

meal_times = {
    'breakfast': range(7, 10),
    'lunch': range(12, 15),
    'dinner': range(19, 22)
}

minutes = [0, 15, 30, 45]

for meal in meal_times:
    results = []

    for h in meal_times[meal]:
        for m in minutes:
            input_dict = {col: 0 for col in X.columns}

            input_dict['hour'] = h
            input_dict['minute'] = m
            input_dict['day_of_week'] = 2 
            input_dict['month'] = 1

            meal_col = f"meal_{meal}"
            if meal_col in input_dict:
                input_dict[meal_col] = 1

            input_df = pd.DataFrame([input_dict])

            pred_val = model.predict(input_df)[0]

            results.append((h, m, pred_val))

    
    results.sort(key=lambda x: x[2], reverse=True)

    print(f"🍽️ {meal.upper()} PEAK TIMES:")

    for r in results[:3]:
        print(f"{r[0]:02d}:{r[1]:02d} → {r[2]:.2f} people")

    print()

#PEAK PLOT

for meal in meal_times:
    times = []
    values = []

    for h in meal_times[meal]:
        for m in minutes:

            input_dict = {col: 0 for col in X.columns}

            input_dict['hour'] = h
            input_dict['minute'] = m
            input_dict['day_of_week'] = 2
            input_dict['month'] = 1

            input_dict[f"meal_{meal}"] = 1

            input_df = pd.DataFrame([input_dict])
            pred_val = model.predict(input_df)[0]

            times.append(f"{h}:{m}")
            values.append(pred_val)

    plt.figure()
    plt.plot(times, values)
    plt.xticks(rotation=45)
    plt.title(f"{meal.capitalize()} Crowd Prediction")
    plt.xlabel("Time")
    plt.ylabel("Predicted Headcount")
    plt.show()