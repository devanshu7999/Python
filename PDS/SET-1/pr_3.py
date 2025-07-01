n = int(input("Enter your number : "))

f1 = 1
f2 = 1
print(f1 , f2 ,end= " ")

for i in range(3,n+1):
    f3 = f1 + f2
    print(f3 ,end=" ")
    f1 = f2
    f2 = f3