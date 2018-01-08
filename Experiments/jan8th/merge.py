import pandas as pd

file1 = pd.read_csv("uniquedata1.csv")
file2 = pd.read_csv("uniquedata2.csv")

merged = file1.merge(file2, on='id')
merged.to_csv("output.csv", index=False)
