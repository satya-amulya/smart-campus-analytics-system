import sqlite3
import pandas as pd
import os

# Connect to (or create) the database
conn = sqlite3.connect("smart_campus.db")
cursor = conn.cursor()

# ─── Create tables ────────────────────────────────────────────────────────────

cursor.executescript("""
CREATE TABLE IF NOT EXISTS attendance (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id  TEXT,
    date        DATE,
    status      TEXT,
    course      TEXT,
    department  TEXT
);

CREATE TABLE IF NOT EXISTS electricity (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp       DATETIME,
    building        TEXT,
    units_consumed  REAL,
    meter_id        TEXT
);

CREATE TABLE IF NOT EXISTS mess (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id  TEXT,
    date        DATE,
    meal_type   TEXT,
    amount      REAL,
    feedback    TEXT
);

CREATE TABLE IF NOT EXISTS wifi (
    id               INTEGER PRIMARY KEY AUTOINCREMENT,
    device_id        TEXT,
    timestamp        DATETIME,
    location         TEXT,
    data_usage_mb    REAL,
    signal_strength  REAL
);
""")

# ─── Load CSVs into tables ────────────────────────────────────────────────────

data_dir = "data/data_files"   # adjust this path if needed

csv_table_map = {
    "attendance_cleaned.csv": "attendance",
    "electricity_clean.csv":  "electricity",
    "mess_clean.csv":         "mess",
    "wifi_cleaned_data.csv":  "wifi",
}

for csv_file, table_name in csv_table_map.items():
    path = os.path.join(data_dir, csv_file)
    if os.path.exists(path):
        df = pd.read_csv(path)
        df.to_sql(table_name, conn, if_exists="replace", index=False)
        print(f"✓ Loaded {len(df)} rows into '{table_name}' from {csv_file}")
    else:
        print(f"⚠  File not found: {path}")

conn.commit()
conn.close()
print("\nDatabase 'smart_campus.db' created successfully.")