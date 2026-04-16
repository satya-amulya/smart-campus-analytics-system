import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

#anomaly for wifi data

df = pd.read_csv('data/data_files/wifi_cleaned_data.csv')

print("Columns:", df.columns)

df = pd.get_dummies(df, columns=['location'])

X = df[['devices_connected', 'hours_used', 'data_usage_mb'] + 
       [col for col in df.columns if col.startswith('location_')]]

 
model = IsolationForest(contamination=0.05)

df['anomaly'] = model.fit_predict(X)

# anomaly = -1 → unusual
anomalies = df[df['anomaly'] == -1]

print("\n Number of anomalies:", len(anomalies))
print("\nSample anomalies:")
print(anomalies.head())

#plot

plt.figure()

normal = df[df['anomaly'] == 1]
plt.scatter(normal['devices_connected'], normal['data_usage_mb'], label='Normal')

# anomalies
plt.scatter(anomalies['devices_connected'], anomalies['data_usage_mb'], label='Anomaly')

plt.xlabel("Devices Connected")
plt.ylabel("Data Usage (MB)")
plt.title("WiFi Anomaly Detection")
plt.legend()

plt.show()

#electricity anomaly detectiom

df_e = pd.read_csv('data/data_files/electricity_clean.csv')

X_e = df_e[['hour', 'kwh']]

model_e = IsolationForest(contamination=0.05)

df_e['anomaly'] = model_e.fit_predict(X_e)

anomalies_e = df_e[df_e['anomaly'] == -1]

print("\n Electricity anomalies:", len(anomalies_e))

#plot

plt.figure()

normal_e = df_e[df_e['anomaly'] == 1]
plt.scatter(normal_e['hour'], normal_e['kwh'], label='Normal')

plt.scatter(anomalies_e['hour'], anomalies_e['kwh'], label='Anomaly')

plt.xlabel("Hour")
plt.ylabel("kWh")
plt.title("Electricity Anomaly Detection")
plt.legend()

plt.show()