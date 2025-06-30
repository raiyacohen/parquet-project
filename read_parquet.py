import pandas as pd

file_path = 'cic-collection.parquet'

# Read the Parquet file
df = pd.read_parquet(file_path)

print(df.head(10)) #print the first 10
print(df.tail(10)) #prints the last 10

print("\nDataset Info:")
print(df.info())

# Get the list of column names
print("\nColumn Names:")
print(df.columns.tolist())

# Count how many of each label there are (e.g., Benign vs Malicious)
print("\nLabel Counts:")
print(df['Label'].value_counts())

# Show summary statistics
print("\nSummary Stats:")
print(df.describe())