# Define Animal - an abstract class with attributes and methods common to all animals
class Animal:
    def __init__(self, name, species):  # common attributes
        self.name = name
        self.species = species

    def speak(self):  # method to demonstrate polymorphism
        pass

    def move(self):
        pass
