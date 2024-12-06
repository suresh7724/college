import pandas as pd
import numpy as np

# Create the DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', None, 'Grace', 'Bob', 'Hannah', 'Eve'],
    'Salary': [50000, 60000, 70000, 80000, None, 45000, 60000, 60000, None, 80000],
    'Department': ['HR', 'Finance', 'IT', 'IT', 'HR', 'HR', None, 'Finance', 'IT', 'HR']
}
df = pd.DataFrame(data)

# Add missing and duplicate values
print("Original DataFrame:")
print(df)

# Drop all rows with null or empty values
df_cleaned = df.dropna()

# Drop duplicate rows
df_cleaned = df_cleaned.drop_duplicates()

print("\nModified DataFrame (After dropping null and duplicate values):")
print(df_cleaned)
