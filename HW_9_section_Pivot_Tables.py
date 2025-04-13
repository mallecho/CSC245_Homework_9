import pandas as pd
import matplotlib.pyplot as plt

# Sample dataset
data = {
    'Region': ['North', 'North', 'South', 'South', 'East', 'East', 'West', 'West'],
    'Product': ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'B'],
    'Quarter': ['Q1', 'Q1', 'Q1', 'Q1', 'Q2', 'Q2', 'Q2', 'Q2'],
    'Sales': [100, 150, 200, 250, 300, 350, 400, 450]
}
df = pd.DataFrame(data)

# 1. Pivot table with multiple levels
pivot_multi = pd.pivot_table(df, values='Sales', index=['Region', 'Product'], columns='Quarter')
print("Pivot Table with Multiple Levels:\n", pivot_multi)

# 2. Pivot table with subtotals
pivot_with_margins = pd.pivot_table(df, values='Sales', index=['Region', 'Product'], columns='Quarter', margins=True, margins_name='Total')
print("\nPivot Table with Subtotals:\n", pivot_with_margins)

# 3. Compare pivot table with groupby
grouped = df.groupby(['Region', 'Product', 'Quarter'])['Sales'].sum().unstack('Quarter')
print("\nGroupby and Aggregation:\n", grouped)

# 4. Function to generate customizable pivot tables
def generate_pivot_table(dataframe, values, index, columns, margins=False):
    return pd.pivot_table(dataframe, values=values, index=index, columns=columns, margins=margins)

custom_pivot = generate_pivot_table(df, values='Sales', index='Region', columns='Quarter', margins=True)
print("\nCustomizable Pivot Table:\n", custom_pivot)

# 5. Use pivot tables for visualization
pivot_for_plot = pd.pivot_table(df, values='Sales', index='Quarter', columns='Region', aggfunc='sum')
print("\nPivot Table for Visualization:\n", pivot_for_plot)

pivot_for_plot.plot(kind='bar', figsize=(10, 6), title="Sales by Region per Quarter")
plt.xlabel('Quarter')
plt.ylabel('Sales')
plt.legend(title='Region')
plt.show()
