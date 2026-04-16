import pandas as pd
import numpy as np
import random

# reproducibility
random.seed(42)
np.random.seed(42)

records = []

# Areas
areas = [
    'A1','A2','A3','A4','A5','A6',
    'B1','B2','B3',
    'C1','C2','C3','C4','C5','C6',
    'Common Area'
]

# function to create time slot
def get_time_slot(hour):
    return f"{hour:02d}:00-{hour+2:02d}:00"

# simulate 60 days
for day in pd.date_range(start='2026-01-01', periods=60):

    for area in areas:

        for hour in range(0, 24, 2):  # every 2 hours

            # A & C blocks + Common Area
            if area.startswith('A') or area.startswith('C') or area == 'Common Area':

                if 20 <= hour <= 23 or 0 <= hour <= 2:
                    base = 70   # night peak 🔥

                elif 12 <= hour <= 16:
                    base = 20   # afternoon low

                else:
                    base = 40   # normal

            # B blocks
            elif area.startswith('B'):

                if 10 <= hour <= 14:
                    base = 80   # peak (11–1 approx) 🔥

                elif 0 <= hour <= 6:
                    base = 15   # night low

                else:
                    base = 35   # normal

            # randomness (±15%)
            kwh = round(np.random.normal(base, base * 0.15), 2)
            kwh = max(0, kwh)

            # create time slot
            time_slot = get_time_slot(hour)

            records.append({
                'date': day.date(),
                'area': area,
                'hour': hour,              # for ML
                'time_slot': time_slot,    # for dashboard
                'kwh': kwh
            })

# create dataframe
df = pd.DataFrame(records)

# save to CSV
df.to_csv('electricity.csv', index=False)

print("✅ Electricity dataset created successfully!")
print(df.head())