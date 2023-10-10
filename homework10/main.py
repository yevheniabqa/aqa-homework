from animal import Animal
from mammal import Mammal
from bird import Bird
from eagle import Eagle
from platypus import Platypus
from reptile import Reptile
from croc import Crocodile
from monkey import Monkey
from capuchin import Capuchin


def main():
    # Create instances of different classes
    lion = Mammal("Simba", "Lion", "Golden")
    hawk = Bird("Hawkeye", "Hawk", "Brown")
    bald_eagle = Eagle("Freedom", "Bald Eagle", "White", "Large")
    platypus = Platypus("Perry", "Platypus", "Brown", True)
    python = Reptile("Monty", "Python", "Green")
    saltwater_crocodile = Crocodile("Snappy", "Saltwater Crocodile", "Gray", "Large")
    chimpanzee = Monkey("Coco", "Chimpanzee", "Brown", "Long")
    capuchin_monkey = Capuchin("Charlie", "Brown", "Long", "High")

    # Demonstrate polymorphism by calling the 'speak' method on various instances
    animals = [lion, hawk, bald_eagle, platypus, python, saltwater_crocodile, chimpanzee, capuchin_monkey]

    for animal in animals:
        print(f"I'm {animal.name} the {animal.species}, I say: {animal.speak()}")


if __name__ == "__main__":
    main()
