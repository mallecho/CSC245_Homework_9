import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Constructing a DataFrame with missing values
data = {
    'A': [1, 2, np.nan, 4],
    'B': [np.nan, 2, 3, 4],
    'C': [1, np.nan, np.nan, 4],
    'D': [np.nan, np.nan, np.nan, np.nan]  # Fully missing column
}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)

# Step 2: Using isnull(), dropna(), and fillna()
print("\nIs null:\n", df.isnull())
print("\nDrop rows with any NaN:\n", df.dropna())
print("\nFill NaN with 0:\n", df.fillna(0))

# Step 3: Forward fill, backward fill, and interpolation for time-indexed data
dates = pd.date_range('2023-01-01', periods=6)
time_data = {
    'Value': [1, np.nan, np.nan, 4, 5, np.nan]
}
time_df = pd.DataFrame(time_data, index=dates)
print("\nTime-indexed DataFrame:\n", time_df)

print("\nForward fill:\n", time_df.ffill())
print("\nBackward fill:\n", time_df.bfill())
print("\nInterpolation:\n", time_df.interpolate())

# Step 4: Dropping rows where a subset of columns have missing values
print("\nDrop rows where A and B have NaN:\n", df.dropna(subset=['A', 'B']))

# Step 5: Creating a function for dtype-based fill strategies
def fill_by_dtype(df):
    for col in df.columns:
        if df[col].dtype == 'float':
            df[col] = df[col].fillna(df[col].mean())  # Fill numeric columns with mean
        else:
            df[col] = df[col].fillna("Unknown")  # Fill non-numeric columns with a placeholder
    return df

# Apply the function
print("\nFill by dtype:\n", fill_by_dtype(df))

# Step 6: Evaluating impact on statistical summaries and plotting
print("\nSummary before filling:\n", df.describe())

filled_df = df.fillna(0)  # Example fill strategy
print("\nSummary after filling:\n", filled_df.describe())

# Plotting
filled_df['A'].fillna(0).plot(kind='bar', title="Filled Data Visualization")
plt.show()
