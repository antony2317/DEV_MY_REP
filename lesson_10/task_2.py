class Math:
    def __init__(self):
        pass

    def addition(self, a, b):
        print(f"{a} + {b} = {a + b}")

    def subtraction(self, a, b):
        print(f"{a} - {b} = {a - b}")

    def multiplication(self, a, b):
        print(f"{a} * {b} = {a * b}")

    def division(self, a, b):
        if b != 0:
            print(f"{a} / {b} = {a / b}")
        else:
            print("Ошибка: Деление на ноль невозможно")

math = Math()
math.addition(10, 5)
math.subtraction(10, 5)
math.multiplication(10, 5)
math.division(10, 5)
math.division(10, 0)
