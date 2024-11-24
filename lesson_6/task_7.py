from random import randint
print(""" Задача № 7
матрица с рандомными числами""")


def matrix():
    r = 0
    x = int(input('введите количество столбцов: '))
    y = int(input('введите количество строк: '))
    arr = []

    for i in range(x):
        arr.append([])
        for j in range(y):
            arr[i].append(randint(0, 100))
            r += 1
    print('матрица')
    for u in range(x):
        print(arr[u])


matrix()
