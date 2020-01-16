import numpy as np

print('\nAddition')
A = np.array([[2, 4], [5, -6]])
B = np.array([[9, -3], [3, 6]])
C = A + B
print(C)

print('\nMultiplication')
A = np.array([[3,6,7], [5, -3, 0]])
B = np.array([[1,1], [2, 1], [3, -3]])
C = A.dot(B)
print(C)


print("\nTranspose Matrix")
A = np.array([[1, 2, 3], [4, 5, 6]])
print(A.transpose())
B = np.array([[1, 2], [3, 4], [5, 6]])
print(B.transpose())

# Access Matrix Elements
# One dimensional Array
A = np.array([1, 2, 3, 4, 5, 6])
print(A)
print(A[0])
print(A[2])
print(A[-1])

# Two dimensional Array
A = np.array([
    [1, 4, 5, 12],
    [-5, 8, 9, 0],
    [-6, 7, 11, 19]
])
print(A[0][3])
print(A[1][0])
print(A[-1][-1])

# Access row of Matrix
print(A[0])
print(A[1])
print(A[-1])

# Access column of Matrix
print(A[:, 0])
print(A[:, 1])
print(A[:, -1])

print('\nSlicing Matrix')
A = np.array([1, 2 ,3, 4, 5, 6, 7, 8, 9])
print(A[1:3])
print(A[:-4])

A = np.array([
    [1, 4, 5, 12, 14],
    [-5, 8, 9, 0, 17],
    [-6, 7, 11, 19, 21]
])
print(A[:2, :4])
print(A[:1])
print(A[:2])
print(A[:, 2:5])
print(A[1:2, 3])
