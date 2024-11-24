from random import random
n = int(input('Введите количество столбцов и строк: '))
matrix = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(int(random()*10))
    matrix.append(row)
for row in matrix:
    print(row)
sum_main = 0
sum_secondary = 0
for i in range(n):
    sum_main += matrix[i][i]
    sum_secondary += matrix[i][n - i - 1]
print(sum_main)
print(sum_secondary)
