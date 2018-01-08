import pandas as pd

file1 = pd.read_csv("data1.csv")
file2 = pd.read_csv("data2_new.csv")

merged = file1.merge(file2, on='id')
merged.to_csv("output.csv", index=False)