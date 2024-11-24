print("""     Задача № 4
Программа находит общий делитель двух чисел""")


def gcd(m, n):
    while m != n:
        if m > n:
            m = m - n
        else:
            n = n - m
    return n


a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
print(gcd(a, b))
