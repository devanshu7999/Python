import pandas as pd

dataFrame = pd.read_csv('C:/Users/Devanshu/Desktop/Python/PDS Manual/SET-5/penguins.csv').head(5)


print(dataFrame)
d = dataFrame.dropna()
print("After removing a nan row")
print(d)

print("after filling nan")
dataFrame = dataFrame.select_dtypes(include='number')

d = dataFrame.fillna(dataFrame.mean())

print(d)

