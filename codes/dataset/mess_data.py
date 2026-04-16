import pandas as pd
import numpy as np
import random
np.random.seed(42)
random.seed(42)
# Function to generate time slots (15 min interval)
def generate_time_slots(start, end):
    return pd.date_range(start=start, end=end, freq='15min').time

# Function to calculate base using smooth curve
def get_base(meal, t):
    minutes = t.hour * 60 + t.minute  # convert time to minutes

    if meal == 'breakfast':
        peak_time = 8 * 60 + 30   # 8:30 AM
        peak_value = 320
        spread = 60

    elif meal == 'lunch':
        peak_time = 13 * 60 + 30  # 1:30 PM
        peak_value = 500
        spread = 60

    else:  # dinner
        peak_time = 20 * 60 + 30  # 8:30 PM
        peak_value = 420
        spread = 60

    # Gaussian (bell curve)
    base = peak_value * np.exp(-((minutes - peak_time) ** 2) / (2 * spread ** 2))

    return base


records = []

# simulate for 60 days
for day in pd.date_range(start='2025-01-14', periods=60):

    meals = {
        'breakfast': generate_time_slots('07:30', '09:30'),
        'lunch': generate_time_slots('12:30', '14:30'),
        'dinner': generate_time_slots('19:30', '21:30')
    }

    for meal, times in meals.items():

        for t in times:

            base = get_base(meal, t)

            # add randomness (±10%)
            headcount = int(np.random.normal(base, base * 0.1))
            headcount = max(0, headcount)

            records.append({
                'date': day.date(),
                'meal': meal,
                'time': t,
                'hour': t.hour,
                'minute': t.minute,
                'headcount': headcount
            })

# create dataframe
df = pd.DataFrame(records)

# save to CSV
df.to_csv('mess_data.csv', index=False)

print("✅ Mess dataset created successfully!")
print(df.head())