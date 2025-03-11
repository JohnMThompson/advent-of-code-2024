import pandas as pd

# Read data from Day 1
df = pd.read_csv('../01/output.csv', index_col=0)

# Create datasets

df1 = df
df2 = df

# Join datasets
df = pd.merge(df1, df2, left_on='col1', right_on='col2', how='left')
df = df[['col1_x', 'col2_y']]

# Remove non-matches
df.dropna(subset=['col2_y'], inplace=True)

# Count rows for each number
row_counts = df.groupby(['col1_x']).count().reset_index()

# Calculate similarity and total
similarity = row_counts['col1_x'] * row_counts['col2_y']
total = similarity.sum()

# Show results
print(total)
