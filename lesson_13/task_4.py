from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

class AnimalFactory:
    def create_animal(self, animal_type: str) -> Animal:
        if animal_type.lower() == "dog":
            return Dog()
        elif animal_type.lower() == "cat":
            return Cat()
        else:
            raise ValueError(f"Неизвестный тип животного{animal_type}")

if __name__ == "__main__":
    factory = AnimalFactory()

    dog = factory.create_animal("dog")
    print(f"Собака говорит {dog.speak()}")

    cat = factory.create_animal("cat")
    print(f"Кот говорит {cat.speak()}")
