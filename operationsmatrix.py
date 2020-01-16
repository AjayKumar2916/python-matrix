a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

b = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

result = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]


print(a)
print(b)

print('\nAddition')
for i in range(len(a)):
    for j in range(len(a[0])):
        result[i][j] = a[i][j] + b[i][j]
print(result)
print([[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))])


print('\nSubtraction')
for i in range(len(a)):
    for j in range(len(a[0])):
        result[i][j] = a[i][j] - b[i][j]
print(result)
print([[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))])


print('\nMultiplication')
for i in range(len(a)):
    for j in range(len(a[0])):
        result[i][j] = a[i][j] * b[i][j]
print(result)
print([[a[i][j] * b[i][j] for j in range(len(a[0]))] for i in range(len(a))])

print('\nDivision')
for i in range(len(a)):
    for j in range(len(a[0])):
        result[i][j] = a[i][j] / b[i][j]
print(result)
print([[a[i][j] / b[i][j] for j in range(len(a[0]))] for i in range(len(a))])


print('\nMatrix Transpose')
x = [
    [1, 2],
    [3, 4],
    [5, 6]
]

r = [
    [0, 0, 0],
    [0, 0, 0]
]

for i in range(len(x)):
    for j in range(len(x[0])):
        r[j][i] = x[i][j]
print(r)

