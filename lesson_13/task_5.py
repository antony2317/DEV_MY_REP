class Calculator:
    def __init__(self):
        self._strategy = None

    def set_strategy(self, strategy):
        self._strategy = strategy

    def calculate(self, a, b):
        if self._strategy is None:
            raise ValueError("Стратегия не установлена")
        return self._strategy.execute(a, b)

class Addition:
    def execute(self, a, b):
        return a + b

class Subtraction:
    def execute(self, a, b):
        return a - b

class Multiplication:
    def execute(self, a, b):
        return a * b

class Division:
    def execute(self, a, b):
        if b == 0:
            raise ValueError("Деление на ноль невозможно")
        return a / b

if __name__ == "__main__":
    calc = Calculator()

    calc.set_strategy(Addition())
    print("Сложение: 5 + 3 =", calc.calculate(5, 3))

    calc.set_strategy(Subtraction())
    print("Вычитание: 5 - 3 =", calc.calculate(5, 3))

    calc.set_strategy(Multiplication())
    print("Умножение: 5 * 3 =", calc.calculate(5, 3))

    calc.set_strategy(Division())
    print("Деление: 6 / 3 =", calc.calculate(6, 3))
