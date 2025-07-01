import pandas as pd

dataFrame1 = pd.DataFrame({'A' : [1,2,3,4,5],'B' : [6,7,8,9,10]})

dataFrame2 = pd.DataFrame({'B' : [6,7,8,9,10,20,30,40],'C' : [11,12,13,14,15,16,17,18]})

mergedData = dataFrame1.merge(dataFrame2,how='outer')
print(mergedData)

print(mergedData.loc[:2,['A','C']])

