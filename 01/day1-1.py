import pandas as pd

# Read data

df = pd.read_csv('input.txt', header=None, names=['col1'])

# Split data into columns
df[['col1', 'col2',]] = df['col1'].str.split(' ', n=1, expand=True)

# Data cleanup and sorting

df1 = df['col1']
df1 = df['col1'].astype(int)
l1 = df1.to_list()
l1 = sorted(l1)

df2 = df['col2']
df2 = df['col2'].astype(int)
l2 = df2.to_list()
l2 = sorted(l2)

# Combine datasets

df = pd.DataFrame(
    {'col1': l1, 
     'col2': l2
    })

# Calculate
df['dif'] = abs(df['col2'] - df['col1'])
total = df['dif'].sum()

print(total)
df.to_csv('output.csv')
