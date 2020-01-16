import numpy as np
a = np.array([1, 2, 3])
print(a)
print(type(a))

x = np.array([[1, 2, 3], [4, 5, 6]])
print(x)
y = np.array([[1.1, 2, 3], [4, 5, 6]])
print(y)
z = np.array([[1, 2, 3], [4, 5, 6]], dtype=complex)
print(z)


# Array of zeros and ones
zerro_array = np.zeros((2, 3))
print(zerro_array)
ones_array = np.ones((2, 2), dtype=np.int32)
print(ones_array)


# Arange() and shape()
A = np.arange(4)
print(A)
B = np.arange(12).reshape(2, 6)
print(B)