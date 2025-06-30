import pandas as pd

file_path = 'cic-collection.parquet'

df = pd.read_parquet(file_path) # read the parquet file "cic-collection.paraquet"

print(df.head(10)) #print the first 10
print(df.tail(10)) #prints the last 10

print("\nDataset Info:")
print(df.info())

print("\nColumn Names:") # to get the list of column names
print(df.columns.tolist())

print("\nLabel Counts:") # to see how many of each label there are (bengin vs malicous)
print(df['Label'].value_counts())

print("\nSummary Stats:") # show summary statistics
print(df.describe())
