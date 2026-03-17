import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/cleaned_transit_ridership.csv")

df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.to_period('M')

monthly = df.groupby('month')['boarding_count'].sum()

monthly.plot()
plt.title("Monthly Ridership")
plt.xlabel("Month")
plt.ylabel("Boarding Count")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("outputs/monthly_ridership.png")
plt.close()

# Ridership by Route
route = df.groupby('route_id')['boarding_count'].sum()

route.plot(kind='bar')
plt.title("Ridership by Route")
plt.xlabel("Route")
plt.ylabel("Boarding Count")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("outputs/ridership_by_route.png")
plt.close()

# Vehicle Utilization
vehicle = df.groupby('vehicle_type')['boarding_count'].mean()

vehicle.plot(kind='bar')
plt.title("Vehicle Utilization")
plt.xlabel("Vehicle Type")
plt.ylabel("Average Boarding")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("outputs/vehicle_utilization.png")
plt.close()

# Weather Impact
weather = df.groupby('weather')['boarding_count'].mean()

weather.plot(kind='bar')
plt.title("Weather Impact")
plt.xlabel("Weather")
plt.ylabel("Average Boarding")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("outputs/weather_impact.png")
plt.close()

# Summary JSON
summary = {
    "total_rows": len(df),
    "total_boardings": int(df['boarding_count'].sum()),
    "average_boardings": float(df['boarding_count'].mean())
}

import json

with open("outputs/summary.json", "w") as f:
    json.dump(summary, f, indent=4)