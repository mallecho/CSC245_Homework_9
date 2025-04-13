import pandas as pd
import numpy as np

# Sample DataFrame with categorical-like columns
data = {
    'Category': ['A', 'B', 'A', 'C', 'B', 'A'],
    'Values': [10, 20, 15, 10, 30, 25],
    'Type': ['X', 'Y', 'X', 'Z', 'Y', 'Z']
}
df = pd.DataFrame(data)

# 1. Convert object columns to category dtype and observe memory usage
print("Before conversion to category dtype:")
print(df.info(memory_usage='deep'))

df['Category'] = df['Category'].astype('category')
df['Type'] = df['Type'].astype('category')

print("\nAfter conversion to category dtype:")
print(df.info(memory_usage='deep'))

# 2. Set and reorder category levels explicitly
df['Category'] = df['Category'].cat.set_categories(['C', 'B', 'A'], ordered=True)

# 3. Perform comparisons and sorting on categorical columns
df_sorted = df.sort_values(by='Category')
print("\nSorted DataFrame by Category:")
print(df_sorted)

# 4. Group by categorical variables and compute stats
grouped_stats = df.groupby('Category').agg({'Values': ['mean', 'sum']})
print("\nGrouped statistics by Category:")
print(grouped_stats)

# 5. Use pd.get_dummies() to one-hot encode categorical features
one_hot_encoded = pd.get_dummies(df, columns=['Category', 'Type'])
print("\nOne-hot encoded DataFrame:")
print(one_hot_encoded)
