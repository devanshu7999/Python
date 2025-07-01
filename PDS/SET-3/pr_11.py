def is_prime(no):
    for i in range(2,no):
        if(no % i == 0):
            return False
        else :
            if(i == no-1):
                return True
            else:
                continue
            

n = int(input("Enter your number : "))

print(list(filter(lambda x : is_prime(x),range(1,n+1))))