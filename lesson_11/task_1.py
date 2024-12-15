class Tovar:
    def __init__(self, name, shop, price):
        self.__name = name
        self.__shop = shop
        self.__price = price

    def get_name(self):
        return self.__name

    def get_shop(self):
        return self.__shop

    def get_price(self):
        return self.__price

    def __str__(self):
        return f"Товар: {self.__name}, Магазин: {self.__shop}, Цена: {self.__price} руб."

    def __add__(self, other):
        if isinstance(other, Tovar):
            return self.__price + other.__price
        raise TypeError("Сложение возможно только между объектами класса Tovar")


class Sklad:
    def __init__(self):
        self.__tovars = []

    def add_tovar(self, tovar):
        if isinstance(tovar, Tovar):
            self.__tovars.append(tovar)
        else:
            raise TypeError("Добавлять можно только объекты класса Tovar")

    def get_tovar_by_index(self, index):
        if 0 <= index < len(self.__tovars):
            print(self.__tovars[index])
        else:
            print("Товар с таким индексом не найден!")

    def get_tovar_by_name(self, name):
        found = False
        for tovar in self.__tovars:
            if tovar.get_name() == name:
                print(tovar)
                found = True
        if not found:
            print("Товар с таким названием не найден!")

    def sort_by_name(self):
        self.__tovars.sort(key=lambda tovar: tovar.get_name())

    def sort_by_shop(self):
        self.__tovars.sort(key=lambda tovar: tovar.get_shop())

    def sort_by_price(self):
        self.__tovars.sort(key=lambda tovar: tovar.get_price())

    def show_all_tovars(self):
        for tovar in self.__tovars:
            print(tovar)


if __name__ == "__main__":
    tovar1 = Tovar("Молоко", "Гиппо", 2)
    tovar2 = Tovar("Хлеб", "Грин", 1.5)
    tovar3 = Tovar("Яблоки", "Евроопт", 5)
    tovar4 = Tovar("Сыр", "Корона", 12)

    sklad = Sklad()

    sklad.add_tovar(tovar1)
    sklad.add_tovar(tovar2)
    sklad.add_tovar(tovar3)
    sklad.add_tovar(tovar4)

    print("Все товары на складе:")
    sklad.show_all_tovars()

    print("\nИнформация о товаре по индексу 1:")
    sklad.get_tovar_by_index(1)

    print("\nИнформация о товаре с названием 'Сыр':")
    sklad.get_tovar_by_name("Сыр")

    print("\nТовары отсортированы по названию:")
    sklad.sort_by_name()
    sklad.show_all_tovars()

    print("\nТовары отсортированы по магазину:")
    sklad.sort_by_shop()
    sklad.show_all_tovars()

    print("\nТовары отсортированы по цене:")
    sklad.sort_by_price()
    sklad.show_all_tovars()

    print("\nСложение цен товаров 'Молоко' и 'Хлеб':")
    total_price = tovar1 + tovar2
    print(f"Общая стоимость: {total_price} руб.")
