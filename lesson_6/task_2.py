print("""     Задача № 2
Программа переводит число из десятичной системы в двоичную""")



def dec_bin(number):
    return bin(number)[2:]


number = int(input('Введите число: '))
print(dec_bin(number))
