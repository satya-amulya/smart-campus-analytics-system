import pandas as pd
import numpy as np
import random


np.random.seed(42)
random.seed(42)

# PARAMETERS
num_students = 500
num_days = 7

names = [f"Student_{i}" for i in range(1, num_students+1)]

branches = ["CSE", "ECE", "ME", "CE", "EE", "PHY", "MATH", "METALLURGY", "CHEMICAL"]

courses = {
    "CSE": ["DSA", "OS", "DBMS","Data Science"],
    "ECE": ["Signals", "semiconductors", "python","MSI"],
    "ME": ["Thermo", "Mechanics", "Fluid dynamics","Data Science"],
    "CE": ["Structures", "Geotech", "Mechanics of materials","MSI"],
    "EE": ["Circuits", "Electromagnetics", "Network Theory","Data Science"],
    "PHY": ["Mechanics and Relativity", "Quantum Mechanics", "Analog Electronics","MSI"],
    "MATH": ["Calculus", "Linear Algebra", "Probability","Data Science"],
    "METALLURGY": ["Extractive Metallurgy", "Physical Metallurgy", "Materials Science","MSI"],
    "CHEMICAL": ["Process Control", "Reactions", "Separation","Data Science"]
}

data = []

dates = pd.date_range(start="2026-04-01", periods=num_days)

for i in range(num_students):
    name = names[i]
    
    enroll = random.randint(20000000, 25999999)
    branch = random.choice(branches)
    
    # FIXED realistic semester mapping
    year_sem = "2-1"
    
    for date in dates:
        day = date.weekday()
        
        # Improved weekly pattern
        if day == 0: prob_base = 0.9      # Monday
        elif day in [1, 2]: prob_base = 0.85
        elif day == 3: prob_base = 0.8
        elif day == 4: prob_base = 0.75
        else: prob_base = 0.5             # Weekend
        
        for course in courses[branch]:
            
            # Add course difficulty effect
            difficulty_factor = random.uniform(-0.1, 0.05)
            
            prob = min(max(prob_base + difficulty_factor, 0.1), 0.95)
            
            present = np.random.choice([1, 0], p=[prob, 1-prob])
            
            data.append([
                name, enroll, branch, date, present, course, year_sem
            ])

df = pd.DataFrame(data, columns=[
    "student_name", "enrollment_number", "branch",
    "date", "present", "course", "year_semester"
])

df.to_csv("attendance.csv", index=False)

print("Attendance dataset created successfully!")

