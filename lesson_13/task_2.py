def cyclic_sequence(sequence):
    while True:
        for number in sequence:
            yield number


if __name__ == "__main__":
    base_sequence = [1, 2, 3]

    try:
        count = int(input("Введите количество чисел для вывода: "))
        if count <= 0:
            raise ValueError("Количество чисел должно быть положительным.")
    except ValueError as e:
        print(f"Ошибка ввода: {e}")
    else:
        generator = cyclic_sequence(base_sequence)
        result = [next(generator) for _ in range(count)]
        print("Результат:", result)
