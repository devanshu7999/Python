#program to write factorial using concepts such as lambda,reduce and comprehension function

def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n - 1)

if __name__ == "__main__":
    n = int(input("Enter a number: "))

    print("The factorial of", n, "is", factorial(n))

