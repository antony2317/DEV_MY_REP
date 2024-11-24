from random import randint

print("""Задача № 12
программа определяет, какие столбцы имеют хотя бы одно
такое же число""")
n = int(input('введите количество столбцов: '))
m = int(input('введите количество строк: '))
h = int(input('Введите число: '))
my_array = [[randint(0, 10) for _ in range(m)] for _ in range(n)]
print(my_array)
for i in range(m):
    for j in range(n):
        if my_array[j][i] == h:
            print('столбец {} имеет цифру {}'.format(i, h))

        else:
            print('такого числа нет')
