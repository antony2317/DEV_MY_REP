class Car:
    def __init__(self, color, car_type, year):
        self.color = color
        self.car_type = car_type
        self.year = year

    def start(self):
        print("Автомобиль заведён")

    def stop(self):
        print("Автомобиль заглушен")

    def set_year(self, year):
        self.year = year
        print(f"Год выпуска автомобиля: {self.year}")

    def set_type(self, car_type):
        self.car_type = car_type
        print(f"Тип автомобиля: {self.car_type}")

    def set_color(self, color):
        self.color = color
        print(f"Цвет автомобиля: {self.color}")


car = Car("красный", "седан", 2020)
car.start()
car.stop()
car.set_year(2003)
car.set_type("внедорожник")
car.set_color("синий")
