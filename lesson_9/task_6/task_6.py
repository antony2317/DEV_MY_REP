import re

def sum_of_numbers_in_file(filename):
    total_sum = 0
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            numbers = re.findall(r'\d+', content)
            total_sum = sum(int(num) for num in numbers)
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    return total_sum


filename = 'input.txt'

result = sum_of_numbers_in_file(filename)
print(f"Сумма всех чисел в файле: {result}")