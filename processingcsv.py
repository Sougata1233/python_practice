import pandas as pd
data = pd.read_csv('./input.csv')
print (data)
# Slice the result for first 5 rows
print (data[0:5]['salary'])
# Use the multi-axes indexing funtion
print (data.loc[:,['salary','name']])
# Use the multi-axes indexing funtion
# print (data.loc[[1,3,5],['salary','name']])
