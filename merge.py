import pandas as pd

# Creating two sample DataFrames
data1 = {'ID': [1, 2, 3], 'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
data2 = {'ID': [1, 2, 4], 'Salary': [50000, 60000, 70000]}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Merging on the 'ID' column
merged_df = pd.merge(df1, df2, on='ID', how='inner')  # Options: 'inner', 'outer', 'left', 'right'

print(merged_df)
