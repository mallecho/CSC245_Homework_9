import pandas as pd
import numpy as np

# 1. Merge datasets with inner and outer joins
data1 = {'ID': [1, 2, 3], 'Value1': ['A', 'B', 'C']}
data2 = {'ID': [3, 4, 5], 'Value2': ['X', 'Y', 'Z']}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

inner_join = pd.merge(df1, df2, on='ID', how='inner')
print("Inner Join:\n", inner_join)

outer_join = pd.merge(df1, df2, on='ID', how='outer')
print("\nOuter Join:\n", outer_join)

# 2. Concatenate DataFrames with keys
df3 = pd.DataFrame({'Value': [10, 20]}, index=['A', 'B'])
df4 = pd.DataFrame({'Value': [30, 40]}, index=['C', 'D'])
concatenated = pd.concat([df3, df4], keys=['Group1', 'Group2'])
print("\nConcatenated DataFrame with MultiIndex:\n", concatenated)

# 3. Join time-indexed DataFrames with forward fill
time_index1 = pd.date_range('2023-01-01', periods=4, freq='D')
time_index2 = pd.date_range('2023-01-02', periods=4, freq='D')
time_df1 = pd.DataFrame({'Value1': [1, 2, 3, 4]}, index=time_index1)
time_df2 = pd.DataFrame({'Value2': [5, 6, 7, 8]}, index=time_index2)

joined_df = time_df1.join(time_df2, how='outer').ffill()
print("\nJoined DataFrame with forward fill:\n", joined_df)

# 4. Function to merge data from multiple sources
def merge_multiple_sources(datasets, key):
    result = datasets[0]
    for dataset in datasets[1:]:
        result = pd.merge(result, dataset, on=key, how='outer')
    return result

data3 = {'ID': [1, 2, 3], 'Value3': [100, 200, 300]}
data4 = {'ID': [2, 3, 4], 'Value4': [400, 500, 600]}
df3 = pd.DataFrame(data3)
df4 = pd.DataFrame(data4)

merged_result = merge_multiple_sources([df1, df2, df3, df4], key='ID')
print("\nMerged Result from Multiple Sources:\n", merged_result)

# 5. Combine data with duplicate indices and resolve conflicts
dup_index_df1 = pd.DataFrame({'Value': [10, 20]}, index=['A', 'B'])
dup_index_df2 = pd.DataFrame({'Value': [15, 25]}, index=['A', 'B'])

combined_df = dup_index_df1.add(dup_index_df2, fill_value=0)
print("\nCombined DataFrame with resolved conflicts (sum):\n", combined_df)

resolved_conflicts = dup_index_df1.combine(dup_index_df2, func=np.maximum)
print("\nCombined DataFrame with resolved conflicts (max):\n", resolved_conflicts)
