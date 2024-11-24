print("""     Задача № 1
Рекурсивный бинарный поиск""")



def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(arr)
target = int(input('Введите число от 1 до 10: '))
result = binary_search_recursive(arr, target, 0, len(arr) - 1)
print(f"Элемент найден на позиции: {result}")
