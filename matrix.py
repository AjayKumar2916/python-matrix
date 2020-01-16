a = [
    [1, 4, 5, 12],
    [-5, 8, 9, 0],
    [-6, 7, 11, 19]
]

print(a)
print(a[1])
print(a[1][2])
print(a[0][-1])

column = []
for row in a:
    # print(row)
    column.append(row[2])

print(column)