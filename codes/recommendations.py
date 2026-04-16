import pandas as pd

# LOAD DATA

mess = pd.read_csv('data/data_files/mess_clean.csv')
electricity = pd.read_csv('data/data_files/electricity_clean.csv')
wifi = pd.read_csv('data/data_files/wifi_cleaned_data.csv')
attendance = pd.read_csv('data/data_files/attendance_cleaned.csv')

print("\n GENERATING RECOMMENDATIONS...\n")

#  MESS RECOMMENDATION

peak_mess = mess.groupby('hour')['headcount'].mean().idxmax()

print(f" Peak mess hour: {peak_mess}:00")

print(" Recommendation: Increase staff and food preparation during peak hours.\n")

#  ELECTRICITY RECOMMENDATION

peak_elec = electricity.groupby('hour')['kwh'].mean().idxmax()
low_elec = electricity.groupby('hour')['kwh'].mean().idxmin()

print(f" Peak electricity usage hour: {peak_elec}:00")
print(f" Lowest electricity usage hour: {low_elec}:00")

print("Recommendation: Reduce power usage during low-demand hours and optimize usage during peak times.\n")

#  WIFI RECOMMENDATION

peak_wifi_loc = wifi.groupby('location')['devices_connected'].mean().idxmax()

print(f" Most crowded WiFi location: {peak_wifi_loc}")

print("Recommendation: Improve WiFi infrastructure or load balancing in high-usage areas.\n")

# 4. ATTENDANCE RECOMMENDATION

low_attendance_course = attendance.groupby('course')['present'].mean().idxmin()

print(f" Lowest attendance course: {low_attendance_course}")
print(" Recommendation: Review teaching methods or schedule for low-attendance courses.\n")

# FINAL NOTE

print(" Recommendations generated based on data insights.")