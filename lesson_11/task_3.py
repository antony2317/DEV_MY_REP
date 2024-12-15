class Bus:
    def __init__(self, max_seats, max_speed):
        self.speed = 0
        self.max_seats = max_seats
        self.max_speed = max_speed
        self.passenger_list = []
        self.seat_map = {i: None for i in range(1, max_seats + 1)}
        self.has_free_seats = True

    def update_free_seats_flag(self):
        self.has_free_seats = None in self.seat_map.values()

    def board_passenger(self, *passengers):
        for passenger in passengers:
            if None not in self.seat_map.values():
                print(f"Нет свободных мест для пассажира {passenger}.")
                continue
            for seat, occupant in self.seat_map.items():
                if occupant is None:
                    self.seat_map[seat] = passenger
                    self.passenger_list.append(passenger)
                    print(f"Пассажир {passenger} занял место {seat}.")
                    break
        self.update_free_seats_flag()

    def disembark_passenger(self, *passengers):
        for passenger in passengers:
            if passenger in self.passenger_list:
                for seat, occupant in self.seat_map.items():
                    if occupant == passenger:
                        self.seat_map[seat] = None
                        self.passenger_list.remove(passenger)
                        print(f"Пассажир {passenger} покинул место {seat}.")
                        break
            else:
                print(f"Пассажира {passenger} нет в автобусе.")
        self.update_free_seats_flag()

    def increase_speed(self, value):
        self.speed = min(self.speed + value, self.max_speed)
        print(f"Скорость увеличена до {self.speed} км/ч.")

    def decrease_speed(self, value):
        self.speed = max(self.speed - value, 0)
        print(f"Скорость уменьшена до {self.speed} км/ч.")

    def __contains__(self, passenger):
        return passenger in self.passenger_list

    def __iadd__(self, passenger):
        self.board_passenger(passenger)
        return self

    def __isub__(self, passenger):
        self.disembark_passenger(passenger)
        return self

    def display_seat_map(self):
        print("\nТекущее состояние мест в автобусе:")
        for seat, occupant in self.seat_map.items():
            print(f"Место {seat}: {occupant if occupant else 'Свободно'}")
        print()


if __name__ == "__main__":
    bus = Bus(max_seats=5, max_speed=70)

    bus += "Иванов"
    bus += "Петров"
    bus += "Сидоров"
    bus.display_seat_map()

    print("Иванов" in bus)
    print("Васильев" in bus)

    bus -= "Петров"
    bus -= "Сидоров"
    bus.display_seat_map()

    bus.increase_speed(50)
    bus.increase_speed(40)
    bus.decrease_speed(30)
    bus.decrease_speed(50)

    bus.display_seat_map()
