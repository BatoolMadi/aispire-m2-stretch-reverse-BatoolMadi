import pandas as pd

df = pd.read_csv("data/transit_ridership.csv")

# Delete
df = df[df['date'].str.contains('Col') == False]

# Dates
df['date'] = pd.to_datetime(df['date'], errors='coerce').dt.strftime('%Y-%m-%d')
df = df.dropna(subset=['date'])

# is_holiday
df['is_holiday'] = df['is_holiday'].astype(str).str.lower()

df['is_holiday'] = df['is_holiday'].replace({
    'yes': True,
    'no': False,
    '1': True,
    '0': False,
    'true': True,
    'false': False
})

# vehicle_type
df['vehicle_type'] = df['vehicle_type'].str.lower().str.strip()

# weather
df['weather'] = df['weather'].str.lower().str.strip()

# delete rows with missing values
df = df.dropna()

# Save cleaned data
df.to_csv("data/cleaned_transit_ridership.csv", index=False)

print("Data cleaned successfully ✅")