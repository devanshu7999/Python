import numpy as np

# Creating an array
arr = np.array([1, 2, 3, np.nan, np.inf, 5, 6])

# a) any() - Check if any element is True
print("a) Any element is True:", np.any(arr))

# b) all() - Check if all elements are True
print("b) All elements are True:", np.all(arr))

# c) isnan() - Check for NaN (Not a Number)
print("c) Elements are NaN:", np.isnan(arr))

# d) isinf() - Check for infinity
print("d) Elements are infinity:", np.isinf(arr))

# e) isfinite() - Check for finite numbers
print("e) Elements are finite:", np.isfinite(arr))

# f) zeros() - Create an array of zeros
zeros_arr = np.zeros((2, 3))
print("f) Zeros array:")
print(zeros_arr)

# g) isreal() - Check if elements are real numbers
print("g) Elements are real numbers:", np.isreal(arr))

# h) iscomplex() - Check if elements are complex numbers
print("h) Elements are complex numbers:", np.iscomplex(arr))

# i) isscalar() - Check if elements are scalar
print("i) Elements are scalar:", np.isscalar(arr[0]))

# j) less() - Check if elements are less than a value
print("j) Elements are less than 4:", arr[arr < 4])

# k) greater() - Check if elements are greater than a value
print("k) Elements are greater than 3:", arr[arr > 3])

# l) less_equal() - Check if elements are less than or equal to a value
print("l) Elements are less than or equal to 3:", arr[arr <= 3])

# m) greater_equal() - Check if elements are greater than or equal to a value
print("m) Elements are greater than or equal to 3:", arr[arr >= 3])

# n) arrange() - Create an array with a range of values
print("n) Arrange array:", np.arange(1, 10, 2))

# Vector functions

# a) reshape() - Reshape an array
print("a) Reshaped array:")
print(np.arange(12).reshape(3, 4))

# b) linspace() - Create an array of evenly spaced values
print("b) LinSpace array:", np.linspace(0, 10, 5))

# c) randint() - Generate random integers
print("c) Random integers:", np.random.randint(1, 10, 5))

# d) dot() - Dot product of two arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print("d) Dot product:", np.dot(arr1, arr2))
