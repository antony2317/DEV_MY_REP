print("""       Задача № 5
Шифр цезаря""")

print("""Введите 1 для шифрования
Введите 2 для дешифрования""")
a = int(input())

while a:

    def shifr():
        alfavit = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        sdvig = int(input('Введите шаг шифрования: '))
        message = input('Введите сообщение: ').upper()
        itog = ''
        for i in message:
            mesto = alfavit.find(i)
            new_mesto = mesto + sdvig
            if i in alfavit:
                itog += alfavit[new_mesto]
            else:
                itog += i
        print(itog)


    def deshifr():
        alfavit = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        sdvig = int(input('Введите шаг дешифрования: '))
        message = input('Введите сообщение: ').upper()
        itog = ''
        for i in message:
            mesto = alfavit.find(i)
            new_mesto = mesto - sdvig
            if i in alfavit:
                itog += alfavit[new_mesto]
            else:
                itog += i
        print(itog)


    if a <= 1:
        print(shifr())
        break
    else:
        print(deshifr())
        break
