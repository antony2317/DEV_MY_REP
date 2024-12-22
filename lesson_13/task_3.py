class Pizza:
    def __init__(self, size, cheese=False, pepperoni=False, mushrooms=False, onions=False, bacon=False):
        self.size = size
        self.cheese = cheese
        self.pepperoni = pepperoni
        self.mushrooms = mushrooms
        self.onions = onions
        self.bacon = bacon

    def __str__(self):
        toppings = []
        if self.cheese:
            toppings.append("Cheese")
        if self.pepperoni:
            toppings.append("Pepperoni")
        if self.mushrooms:
            toppings.append("Mushrooms")
        if self.onions:
            toppings.append("Onions")
        if self.bacon:
            toppings.append("Bacon")

        return f"Pizza(size={self.size}, toppings={', '.join(toppings) if toppings else 'None'})"

class PizzaBuilder:
    def __init__(self, size):
        self.size = size
        self.cheese = False
        self.pepperoni = False
        self.mushrooms = False
        self.onions = False
        self.bacon = False
    def add_cheese(self):
        self.cheese = True
        return self

    def add_pepperoni(self):
        self.pepperoni = True
        return self

    def add_mushrooms(self):
        self.mushrooms = True
        return self

    def add_onions(self):
        self.onions = True
        return self

    def add_bacon(self):
        self.bacon = True
        return self

    def build(self):
        return Pizza(
            size=self.size,
            cheese=self.cheese,
            pepperoni=self.pepperoni,
            mushrooms=self.mushrooms,
            onions=self.onions,
            bacon=self.bacon
        )

pizza_builder = PizzaBuilder(size="Large")
pizza = (pizza_builder
         .add_cheese()
         .add_pepperoni()
         .add_onions()
         .build())

print(pizza)
