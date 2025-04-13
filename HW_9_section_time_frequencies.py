import pandas as pd
import numpy as np

# 1. Convert between string dates and datetime objects
date_strings = ["2023-01-01", "2023-02-01", "2023-03-01"]
date_objects = pd.to_datetime(date_strings)  # Convert to datetime
print("Converted Date Objects:")
print(date_objects)

# 2. Generate time ranges with custom frequency
custom_range = pd.date_range("2023-01-01", "2023-01-10", freq="2D")  # Every 2 days
print("\nCustom Time Range (Every 2 Days):")
print(custom_range)

# 3. Demonstrate upsampling and downsampling
# Create a time series for demonstration
time_series = pd.Series(
    np.random.rand(10),
    index=pd.date_range("2023-01-01", periods=10, freq="D")
)

# Upsampling (increase frequency)
upsampled = time_series.resample("H").interpolate(method="linear")  # Upsample to hourly with linear interpolation
print("\nUpsampled Time Series (Hourly):")
print(upsampled)

# Downsampling (reduce frequency)
downsampled = time_series.resample("M").mean()  # Downsample to monthly mean
print("\nDownsampled Time Series (Monthly):")
print(downsampled)

# 4. Use asfreq() to set frequency explicitly
asfreq_series = time_series.asfreq("D", method="pad")  # Explicit daily frequency with forward fill
print("\nTime Series with Explicit Frequency (Daily):")
print(asfreq_series)

# 5. Apply shifting and differencing operations
shifted_series = time_series.shift(1)  # Shift forward by 1 day
differenced_series = time_series.diff(1)  # Compute day-to-day differences

print("\nShifted Time Series (1 Day Forward):")
print(shifted_series)
print("\nDifferenced Time Series (Day-to-Day):")
print(differenced_series)
