import pandas as pd

# Step 1: Create a sample DataFrame with text data
data = {
    'Name': [' Alice ', ' Bob', 'Charlie ', '  Dave '],
    'Email': ['alice@example.com', 'bob_at_example.com', 'charlie123@example.net', 'dave99@gmail.com'],
    'Address': ['123 Main St.', '456 Elm St.', '789 Maple Ave.', '101 Oak Blvd.'],
    'Age': ['25', '34 years', 'Unknown', '29']
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Step 2: Clean text data using vectorized string operations
# Clean 'Name' column
df['Name'] = df['Name'].str.strip().str.lower().str.replace(' ', '_')

# Clean 'Age' column by removing non-numeric characters and converting to integers where possible
df['Age'] = df['Age'].str.extract(r'(\d+)')  # Use raw string for regex pattern
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')  # Convert to numeric, NaN for invalid entries

print("\nCleaned DataFrame:")
print(df)

# Step 3: Use regex to extract structured data
# Extract domain names from 'Email'
df['Email_Domain'] = df['Email'].str.extract(r'@([a-zA-Z0-9.-]+)')  # Use raw string for regex pattern

print("\nDataFrame with Extracted Domain:")
print(df)

# Step 4: Perform filtering based on string patterns
# Filter rows where Email contains 'example'
filtered_df = df[df['Email'].str.contains(r'example', na=False)]  # Use raw string for regex pattern

print("\nFiltered DataFrame (Email contains 'example'):")
print(filtered_df)

# Step 5: Concatenate string columns and format output
# Concatenate 'Name' and 'Address' with formatting
df['Full_Info'] = df['Name'].str.title() + ' | ' + df['Address']

print("\nDataFrame with Concatenated String Column:")
print(df)

# Step 6: Apply .str.get() and .str.len() to analyze string content
# Extract the first character of 'Name'
df['First_Character'] = df['Name'].str.get(0)

# Calculate the length of 'Address'
df['Address_Length'] = df['Address'].str.len()

print("\nDataFrame with String Analysis Columns:")
print(df)
