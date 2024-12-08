import json
import csv
import os

# Пути к файлам
JSON_FILE = "employees.json"
CSV_FILE = "employees.csv"

# Проверка существования файлов
def ensure_files_exist():
    # Создаем пустой JSON-файл, если его нет
    if not os.path.exists(JSON_FILE):
        with open(JSON_FILE, "w", encoding="utf-8") as file:
            json.dump([], file, ensure_ascii=False, indent=4)
    # Создаем пустой CSV-файл, если его нет
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", encoding="utf-8", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Имя", "Возраст", "Язык программирования", "Год рождения", "Рост"])

# Чтение данных из JSON
def read_json():
    with open(JSON_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

# Запись данных в JSON
def write_json(data):
    with open(JSON_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# Преобразование данных из JSON в CSV
def json_to_csv():
    data = read_json()
    with open(CSV_FILE, "w", encoding="utf-8", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Имя", "Возраст", "Язык программирования", "Год рождения", "Рост"])
        for employee in data:
            writer.writerow([employee["name"], employee["age"], employee["language"], employee["year"], employee["height"]])
    print("Данные успешно сохранены в CSV.")

# Добавление нового сотрудника в JSON
def add_employee_to_json():
    data = read_json()
    print("Введите данные нового сотрудника:")
    name = input("Имя: ")
    age = int(input("Возраст: "))
    language = input("Язык программирования: ")
    year = int(input("Год рождения: "))
    height = float(input("Рост: "))
    new_employee = {
        "name": name,
        "age": age,
        "language": language,
        "year": year,
        "height": height
    }
    data.append(new_employee)
    write_json(data)
    print("Сотрудник добавлен в JSON-файл.")

# Добавление нового сотрудника в CSV
def add_employee_to_csv():
    print("Введите данные нового сотрудника:")
    name = input("Имя: ")
    age = int(input("Возраст: "))
    language = input("Язык программирования: ")
    year = int(input("Год рождения: "))
    height = float(input("Рост: "))
    with open(CSV_FILE, "a", encoding="utf-8", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, age, language, year, height])
    print("Сотрудник добавлен в CSV-файл.")

# Поиск сотрудника по имени
def search_by_name():
    name = input("Введите имя для поиска: ")
    data = read_json()
    found = False
    for employee in data:
        if employee["name"].lower() == name.lower():
            print(f"Найден сотрудник: {employee}")
            found = True
            break
    if not found:
        print("Сотрудник с таким именем не найден.")

# Фильтр по языку программирования
def filter_by_language():
    language = input("Введите язык программирования: ")
    data = read_json()
    filtered = [employee for employee in data if employee["language"].lower() == language.lower()]
    if filtered:
        print("Список сотрудников, знающих", language)
        for employee in filtered:
            print(employee)
    else:
        print("Нет сотрудников, владеющих этим языком программирования.")

# Фильтр по году рождения и средний рост
def average_height_by_year():
    year = int(input("Введите год рождения: "))
    data = read_json()
    filtered = [employee for employee in data if employee["year"] < year]
    if filtered:
        average_height = sum(employee["height"] for employee in filtered) / len(filtered)
        print(f"Средний рост сотрудников, родившихся до {year}: {average_height:.2f}")
    else:
        print("Нет сотрудников, родившихся до этого года.")

# Главное меню
def main_menu():
    ensure_files_exist()
    while True:
        print("\nВыберите действие:")
        print("1. Преобразовать JSON в CSV")
        print("2. Добавить нового сотрудника в JSON")
        print("3. Добавить нового сотрудника в CSV")
        print("4. Найти сотрудника по имени")
        print("5. Фильтр по языку программирования")
        print("6. Средний рост по году рождения")
        print("7. Выйти из программы")
        choice = input("Введите номер действия: ")

        if choice == "1":
            json_to_csv()
        elif choice == "2":
            add_employee_to_json()
        elif choice == "3":
            add_employee_to_csv()
        elif choice == "4":
            search_by_name()
        elif choice == "5":
            filter_by_language()
        elif choice == "6":
            average_height_by_year()
        elif choice == "7":
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод. Попробуйте снова.")

# Точка входа в программу
if __name__ == "__main__":
    main_menu()
