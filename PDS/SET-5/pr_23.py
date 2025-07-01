import pandas as pd

try:
    dataFrame = pd.read_csv('C:/Users/Devanshu/Desktop/Python/PDS Manual/SET-5/penguins.csv')
except FileNotFoundError:
    print("File not found.")


dataFrame = dataFrame.select_dtypes(include=['number'])

print("DataFrame description:")
print(dataFrame.describe())

print("\nMaximum value in each column:")
print(dataFrame.max())

print("\nMinimum value in each column:")
print(dataFrame.min())

print("\nMean of each column:")
print(dataFrame.mean())

print("\nMedian of each column:")
print(dataFrame.median())

print("\nStandard deviation of each column:")
print(dataFrame.std())

print("\nCorrelation between columns:")
print(dataFrame.corr())
