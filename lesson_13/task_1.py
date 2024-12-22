def fibonacci_sequence(limit):
    a, b = 0, 1
    for _ in range(limit):
        yield a
        a, b = b, a + b


def main():
    try:
        n = int(input("Введите номер числа Фибоначчи, до которого нужно вывести последовательность: "))
        if n <= 0:
            print("Пожалуйста, введите положительное целое число.")
            return

        print("Последовательность Фибоначчи:")
        for number in fibonacci_sequence(n):
            print(number, end=" ")
    except ValueError:
        print("Ошибка ввода! Пожалуйста, введите целое число.")


main()
