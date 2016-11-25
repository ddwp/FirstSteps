print("xyu")
print("hello_world")
x = []
# [0, 10)
for i in range(0, 11):
    x.append(i)
print(x)
y = []
for i in range(0, 11):
    if i % 2 == 0:
        y.append(i)
print(y)
print(y[2])

matrix = []

for i in range(0, 5):
    matrix.append([])
    for j in range(0, 5):
        if i == j:
            matrix[i].append(1)
        else:
            matrix[i].append(0)
for i in range(0, len(matrix)):
    for j in range(0, len(matrix[i])):
        print(matrix[i][j], " ", end="")

    print()