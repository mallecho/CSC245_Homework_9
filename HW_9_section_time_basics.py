import matplotlib.pyplot as plt
import pandas as pd
import numpy as np  # Importing NumPy

# 1. Create a time-indexed Series and plot it
time_series = pd.Series(
    np.random.rand(100),  # Generating 100 random numbers
    index=pd.date_range("2023-01-01", periods=100, freq="D")
)

plt.figure(figsize=(10, 5))
plt.plot(time_series, label='Random Data')
plt.title("Time-Indexed Series")
plt.xlabel("Date")
plt.ylabel("Value")
plt.legend()
plt.show()

# 2. Slice the time series by date range
sliced_series = time_series["2023-01-15":"2023-02-15"]
print("\nSliced Time Series:")
print(sliced_series)

# 3. Resample the data to different frequencies
resampled_mean = time_series.resample("W").mean()  # Weekly mean
resampled_sum = time_series.resample("W").sum()  # Weekly sum
print("\nResampled Time Series (Weekly):")
print("Mean:\n", resampled_mean)
print("Sum:\n", resampled_sum)

# 4. Compute rolling statistics (mean, std)
rolling_mean = time_series.rolling(window=7).mean()
rolling_std = time_series.rolling(window=7).std()

plt.figure(figsize=(10, 5))
plt.plot(time_series, label='Original Data')
plt.plot(rolling_mean, label='7-Day Rolling Mean', color='orange')
plt.plot(rolling_std, label='7-Day Rolling Std', color='green')
plt.title("Rolling Statistics")
plt.xlabel("Date")
plt.ylabel("Value")
plt.legend()
plt.show()

# 5. Handle missing time points and perform interpolation
time_series_with_missing = time_series.copy()
time_series_with_missing.iloc[::10] = np.nan  # Introduce missing values
print("\nTime Series with Missing Data:")
print(time_series_with_missing)

interpolated_series = time_series_with_missing.interpolate(method='linear')
print("\nInterpolated Time Series:")
print(interpolated_series)

plt.figure(figsize=(10, 5))
plt.plot(time_series_with_missing, label='Data with Missing Points', color='red')
plt.plot(interpolated_series, label='Interpolated Data', color='blue')
plt.title("Handling Missing Time Points")
plt.xlabel("Date")
plt.ylabel("Value")
plt.legend()
plt.show()
