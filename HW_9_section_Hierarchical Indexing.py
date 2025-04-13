import pandas as pd
import numpy as np

#Create MultiIndex and build DataFrame
arrays = [
    ['Group1', 'Group1', 'Group2', 'Group2'],
    ['Subgroup1', 'Subgroup2', 'Subgroup1', 'Subgroup2']
]
index = pd.MultiIndex.from_arrays(arrays, names=('Group', 'Subgroup'))

data = {
    'Value1': [10, 20, 30, 40],
    'Value2': [15, 25, 35, 45]
}
df = pd.DataFrame(data, index=index)
print("DataFrame with MultiIndex:\n", df)

# Slice and filter MultiIndex
print("\nSlicing data from Group1:\n", df.loc['Group1'])
print("\nFiltering Subgroup1 across all groups:\n", df.xs('Subgroup1', level='Subgroup'))

# Step 3: Swap and sort index levels
swapped_df = df.swaplevel('Group', 'Subgroup')
print("\nDataFrame with swapped levels:\n", swapped_df)

sorted_df = swapped_df.sort_index()
print("\nDataFrame with sorted index:\n", sorted_df)

# Unstack and stack data
unstacked_df = df.unstack(level='Subgroup')
print("\nUnstacked DataFrame:\n", unstacked_df)

# Stack data back to original format using the future_stack argument
stacked_df = unstacked_df.stack(level='Subgroup', future_stack=True)
print("\nRestored original format:\n", stacked_df)

# Step 5: Groupby on hierarchical data and aggregate
grouped_sum = df.groupby(level='Group').sum()
print("\nSum of values grouped by Group:\n", grouped_sum)

grouped_mean = df.groupby(level=['Group', 'Subgroup']).mean()
print("\nMean values grouped by Group and Subgroup:\n", grouped_mean)
