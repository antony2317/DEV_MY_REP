class BeeElephant:
    def __init__(self, bee: int, elephant: int):
        self.bee = max(0, min(100, bee))
        self.elephant = max(0, min(100, elephant))

    def Fly(self) -> bool:
        return self.bee >= self.elephant

    def Trumpet(self) -> str:
        if self.elephant >= self.bee:
            return "tu-tu-doo-doo"
        else:
            return "wzzzz"

    def Eat(self, meal: str, value: int):
        if meal not in ("nectar", "grass"):
            raise ValueError("Meal must be either 'nectar' or 'grass'")

        if meal == "nectar":
            self.elephant = max(0, self.elephant - value)
            self.bee = min(100, self.bee + value)
        elif meal == "grass":
            self.bee = max(0, self.bee - value)
            self.elephant = min(100, self.elephant + value)


if __name__ == "__main__":
    creature = BeeElephant(bee=30, elephant=50)

    print("Может ли летать?", creature.Fly())
    print("Звук:", creature.Trumpet())

    creature.Eat("nectar", 20)
    print("Если съел нектар:")
    print("Пчела:", creature.bee)
    print("Слон:", creature.elephant)

    creature.Eat("grass", 10)
    print("Если съел траву:")
    print("Пчела:", creature.bee)
    print("Слон:", creature.elephant)
