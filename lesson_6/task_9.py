from random import randint

print("""задача № 9
программа определяет какую долю в общей сумме
(процент) составляет сумма элементов каждого столбца""")
n = int(input('введите количество столбцов: '))
m = int(input('введите количество строк: '))
arr = [[randint(1, 100) for j in range(m)] for i in range(n)]

sum_col = [0] * m
for i in range(n):
    for j in range(m):
        sum_col[j] += arr[i][j]

s = sum(sum_col)
for j in range(m):
    sum_col[j] = round(sum_col[j] / s, 3)
arr.append(sum_col)

for row in arr:
    print(*row)
