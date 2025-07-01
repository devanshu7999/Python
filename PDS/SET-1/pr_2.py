import math

def find_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    
    # Check if roots are real
    if discriminant < 0:
        return "Roots are imaginary"
    elif discriminant == 0:
        root = -b / (2*a)
        return "Root is:", root
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return "Roots are:", root1, root2

# Example usage
a = float(input("Enter the coefficient of x^2: "))
b = float(input("Enter the coefficient of x: "))
c = float(input("Enter the constant term: "))
                #2 -5  2
print(find_roots(a, b, c))
