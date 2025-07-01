oneDList = []
def oneD(l):
    for i in l:
        if(type(i) == tuple or type(i) == list):
            oneD(i)
        else:
            oneDList.append(i)
    return oneDList


li = [1,[2,3],[4,5,('abc','b')]]
print(oneD(li))

