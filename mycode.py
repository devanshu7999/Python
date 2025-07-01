from itertools import permutations
count=0
data=["apple","banana","orange"]
perm = permutations(data,2)
for i in list(perm):
    print(i)
    count+=1
print("Permutation Count",count)