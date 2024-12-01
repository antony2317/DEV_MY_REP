print('Для завершения программы введите 0')

while True:
    s = input('Выберете математическую операцию (+, -, *, /): ')
    if s == '0':
        break
    if s in ('+', '-', '*', '/'):
        try:
            a = float(input('Введите первое: '))
            b = float(input('Введите второе число: '))
            if s == '+':
                print(f'{a + b}')
            elif s == '-':
                print(f'{a - b}')
            elif s == '*':
                print(f'{a * b}')
            elif s == '/':
                if b != 0:
                    print(f'{a / b}')
                else:
                    print('Деление на ноль!')
        except (ValueError, TypeError):
            print('вы ввели не верные данные')
    else:
        print('Неверный знак операции!')
