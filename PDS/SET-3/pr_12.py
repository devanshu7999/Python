from functools import reduce
n =  int(input("Enter your number : "))


print(reduce(lambda prev,curr:prev+curr,range(1,n+1)))
