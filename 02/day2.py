import pandas as pd 
import numpy as np 

# Day 2 Part 1

# Read input
df = pd.read_csv('input.txt', header=None, names=['col1'])
df = df['col1'].str.split(' ')

# Criteria:
# Must increase/decrease but not by more than 3

def compare_adjacent(data):
    result = []
    for i in range(len(data)-1):
        x = int(data[i])
        y = int(data[i + 1])
        result.append(y - x)
    return result

all_results = []

for row in df:
    result_list = compare_adjacent(row)
    all_results.append(result_list)

def check_conditions(data, upper, lower):
    for element in data:
        int(element)
        if element < lower or element > upper or element == 0:
            return False
    return True

# Criteria:
# All values must ascend or descend

def check_increasing(data):
    return not min(data) < 0 < max(data)

# Combine criteria

tf = []

for list in all_results:
    tf_result = check_conditions(list, 3, -3), check_increasing(list)
    tf.append(tf_result)

# Evaluate if both criteria are true

final = []

for item in tf:
    if item[0] == True and item[1] == True:
        final.append(True)
    else:
        final.append(False)

# Count final result

print(sum(final))
