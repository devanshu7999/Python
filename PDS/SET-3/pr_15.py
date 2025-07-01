def deposit(amount):
    global balance
    balance = balance + amount

def withdraw(amount):
    global balance
    if balance > amount:
        balance = balance - amount
    else :
        print('insufficent funds')

def check_balance():
    print(balance)

balance = int(input("Enter your balance : "))

deposit(500)

withdraw(700)

check_balance()