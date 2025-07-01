try:
    with open("non_existing_file.txt", "r") as file:
        data = file.read()

    print(undefined_variable)

    number = int("abc")
    
except IOError:
    print("An IOError occurred: File not found or cannot be opened.")

except NameError:
    print("A NameError occurred: Variable is not defined.")

except ValueError:
    print("A ValueError occurred: Cannot convert string to integer.")

except Exception as e:
    print("An unexpected error occurred:", e)
