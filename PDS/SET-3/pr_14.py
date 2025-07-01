import math

def calculate_area(shape, *args):
    if shape == "rectangle":
        if len(args) != 2:
            raise ValueError("Rectangle requires width and height.")
        width, height = args
        return width * height
    
    elif shape == "circle":
        if len(args) != 1:
            raise ValueError("Circle requires radius.")
        radius = args[0]
        return math.pi * radius ** 2
    
    elif shape == "trapezoid":
        if len(args) != 3:
            raise ValueError("Trapezoid requires base1, base2, and height.")
        base1, base2, height = args
        return 0.5 * (base1 + base2) * height
    
    else:
        raise ValueError("Unknown shape.")

try:
    print("Rectangle area:", calculate_area("rectangle", 10, 20))  
    print("Circle area:", calculate_area("circle", 7))  
    print("Trapezoid area:", calculate_area("trapezoid", 5, 7, 10))  
except ValueError as e:
    print(e)
