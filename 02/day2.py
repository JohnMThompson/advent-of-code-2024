import pandas as pd 

# Read input
df = pd.read_csv('input.txt', header=None, names=['col1'])

df = df['col1'].str.split(' ')
df = df.head(10)

def compare_adjacent(data):
    for i in range(len(data)-1):
        if data[i] == data[i + 1]:
            print('first')
        elif data[i] < data[i+1]:
            print('second')
        else:
            print('third')

for x in df:
    compare_adjacent(x)
    


# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three.
