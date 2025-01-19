import numpy as np
import pandas as pd

# Generate time series
np.random.seed(42)
time_index = pd.date_range(start="2022-01-01", end="2024-12-31 23:00", freq="H")

# Simulate daily and seasonal patterns
daily_pattern = 10 + 5 * np.sin(2 * np.pi * time_index.hour / 24)
seasonal_pattern = 50 + 20 * np.sin(2 * np.pi * (time_index.dayofyear / 365))

# Add random noise
noise = np.random.normal(0, 5, len(time_index))

# Add weekend effect
weekend_effect = np.where(time_index.dayofweek >= 5, -5, 0)

# Add more holidays for realism
holiday_dates = pd.date_range("2022-01-01", "2024-12-31", freq="1D")
holidays_per_year = 30
np.random.seed(42)
selected_holidays = np.random.choice(holiday_dates, holidays_per_year * 3, replace=False)
selected_holidays = pd.to_datetime(selected_holidays)
holiday_effect = np.where(time_index.isin(selected_holidays), -10, 0)

# Combine components
synthetic_load = daily_pattern + seasonal_pattern + noise + weekend_effect + holiday_effect

# Create DataFrame
synthetic_data = pd.DataFrame({
    "Datetime": time_index,
    "Load (kW)": synthetic_load,
    "Temperature (°C)": 15 + 10 * np.sin(2 * np.pi * time_index.dayofyear / 365) + np.random.normal(0, 3, len(time_index)),
    "Humidity (%)": 50 + 30 * np.sin(2 * np.pi * time_index.dayofyear / 365) + np.random.normal(0, 5, len(time_index)),
    "Wind Speed (m/s)": np.random.uniform(0, 10, len(time_index)),
    "Day of Week": time_index.dayofweek,
    "Hour": time_index.hour
})

# Save dataset
file_path = "synthetic_power_load_data_realistic.csv"
synthetic_data.to_csv(file_path, index=False)
file_path
