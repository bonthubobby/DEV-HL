fileread = open("MOCK_DATA.csv")
for val in filread:
eachrow = val.split(",")
if(eacrow[1].startswith("A")):
print(eachrow[1])
if(eachrow[3]).endswith("@amazon.com")):
print(eachrow[3])

