import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample dataset
data = {
    'Category': ['A', 'A', 'B', 'B', 'C', 'C'],
    'Subcategory': ['X', 'Y', 'X', 'Y', 'X', 'Y'],
    'Value1': [10, 20, 30, 40, 50, 60],
    'Value2': [5, 10, 15, 20, 25, 30]
}
df = pd.DataFrame(data)

# 1. Group by one and two categorical columns
grouped_one = df.groupby('Category').agg({'Value1': 'sum', 'Value2': 'mean'})
print("Grouped by one column:\n", grouped_one)

grouped_two = df.groupby(['Category', 'Subcategory']).agg({'Value1': 'sum', 'Value2': 'mean'})
print("\nGrouped by two columns:\n", grouped_two)

# 2. Use .agg() to apply custom functions
custom_agg = df.groupby('Category').agg({
    'Value1': lambda x: x.max() - x.min(),
    'Value2': lambda x: np.std(x)
})
print("\nCustom aggregation:\n", custom_agg)

# 3. Compute normalized statistics
group_means = df.groupby(['Category', 'Subcategory'])['Value1'].mean()
df['Normalized_Value1'] = df['Value1'] / df.set_index(['Category', 'Subcategory']).index.map(group_means)
print("\nDataset with normalized statistics:\n", df)

# 4. Use .filter() on groups based on condition
filtered = df.groupby('Category').filter(lambda x: x['Value1'].sum() > 50)
print("\nFiltered groups where sum of Value1 > 50:\n", filtered)

# 5. Combine groupby with sorting and visualization
grouped_summary = df.groupby('Category').agg({'Value1': 'sum'}).sort_values('Value1', ascending=False)
print("\nGrouped summary sorted by Value1:\n", grouped_summary)

grouped_summary.plot(kind='bar', title='Category-wise Sum of Value1', legend=False)
plt.xlabel('Category')
plt.ylabel('Sum of Value1')
plt.show()
