import pandas as pd
import numpy as np
import random
np.random.seed(42)
random.seed(42)

n = 300

enrollment_numbers = [np.random.randint(20000000, 25999999) for _ in range(n)]

locations = ["Block A", "Block B", "Block C", "Canteen","visitor room" , "Common area"]

data = []

for i in range(n):
    
    enrollment = enrollment_numbers[i]
    
    devices = np.random.randint(1, 4)
    
    # Random hour
    hour = np.random.randint(0, 24)
    
    # Convert to 2-hour slot
    start = (hour // 2) * 2
    end = start + 2
    
    time_slot = f"{start:02d}:00-{end:02d}:00"
    
    # Base hours used
    hours = round(np.random.uniform(0.5, 8), 2)
    
    location = np.random.choice(locations)
    
    #  LOCATION LOGIC
    if location in ["Hostel A", "Hostel B"]:
        hours += np.random.uniform(1, 2)
    
    if location == "Academic Block":
        hours *= 0.5
    
    #  TIME-BASED LOGIC 
    if 18 <= hour <= 22:   # evening peak
        hours += np.random.uniform(1, 2)
    elif 12 <= hour <= 17: # afternoon low
        hours *= 0.7
    
    # Data usage
    data_usage = devices * hours * np.random.uniform(100, 300)
    
    # Heavy users
    if np.random.rand() < 0.1:
        data_usage *= 2
    
    data.append([
        enrollment,
        devices,
        round(hours, 2),
        round(data_usage, 2),
        location,
        time_slot
    ])

df = pd.DataFrame(data, columns=[
    "enrollment_no",
    "devices_connected",
    "hours_used",
    "data_usage_mb",
    "location",
    "time_slot"
])

df.to_csv("wifi_dataset.csv", index=False)

print("CSV with 2-hour time slots created successfully!")