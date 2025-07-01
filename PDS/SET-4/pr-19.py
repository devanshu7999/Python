class StringLengthError(Exception):
    pass

def check(str):
    if len(str) < 2 or len(str) > 6:
        raise StringLengthError("String length must be between 2 and 6 characters")

try:
    string = input("Enter a string: ")
    check(string)
    print("String length is valid.")
except StringLengthError as e:
    print("Error:", e)
