def is_armstrong(no):
    sum  = 0
    for i in no:
        sum = sum + int(i)**3
    if(str(sum) == no):
        return True
    return False

n = int(input('Enter your number : '))

print(list(filter(lambda x : is_armstrong(str(x)),range(1,n+1))))