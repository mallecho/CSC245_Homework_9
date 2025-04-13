import pandas as pd
import numpy as np

# Step 1: Create a large sample DataFrame for demonstration
df = pd.DataFrame({
    'A': np.random.rand(1000000),  # 1 million random floats
    'B': np.random.rand(1000000),  # 1 million random floats
    'Category': np.random.choice(['X', 'Y', 'Z'], size=1000000),  # Random categories
    'Value': np.random.randint(1, 100, size=1000000)  # Random integers
})

# Step 2: Use eval() to perform arithmetic operations on columns
# Standard operation
df['Sum_Standard'] = df['A'] + df['B']

# Using eval() for the same operation
df.eval('Sum_Eval = A + B', inplace=True)

# Step 3: Compare performance of eval() vs standard operations using %timeit
print("\nPerformance comparison of eval() vs standard operations:")
# Uncomment the lines below to run in an interactive environment supporting %timeit
# %timeit df['Sum_Standard'] = df['A'] + df['B']
# %timeit df.eval('Sum_Eval = A + B', inplace=True)

# Step 4: Use query() to filter large DataFrames efficiently
# Standard filtering
filtered_standard = df[df['A'] > 0.5]

# Using query()
filtered_query = df.query('A > 0.5')

# Compare performance of query() vs standard filtering
print("\nPerformance comparison of query() vs standard filtering:")
# Uncomment the lines below to run in an interactive environment supporting %timeit
# %timeit df[df['A'] > 0.5]
# %timeit df.query('A > 0.5')

# Step 5: Optimize memory usage using categorical and appropriate numeric dtypes
print("\nOptimizing memory usage:")
print("Before optimization:")
print(df.info(memory_usage='deep'))  # Show memory usage before optimization

# Convert 'Category' column to category dtype to reduce memory usage
df['Category'] = df['Category'].astype('category')

# Convert float columns to float32
df['A'] = df['A'].astype('float32')
df['B'] = df['B'].astype('float32')

# Convert integer columns to int8 (since values are small)
df['Value'] = df['Value'].astype('int8')

print("After optimization:")
print(df.info(memory_usage='deep'))  # Show reduced memory usage

# Step 6: Benchmark operations using %timeit
print("\nBenchmarking common operations:")
# Uncomment the lines below to run in an interactive environment supporting %timeit
# %timeit df['Sum_Standard'] = df['A'] + df['B']
# %timeit df.query('A > 0.5')
# %timeit df['Category'].value_counts()

print("\nCode execution completed successfully.")
