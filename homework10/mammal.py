from animal import Animal


# Define 'Mammal' is a child class of 'Animal'
class Mammal(Animal):
    def __init__(self, name, species, fur_color):
        super().__init__(name, species)
        self.fur_color = fur_color

    def speak(self):
        return "I'm a mammal, I can make various sounds"

    def feed_milk(self):
        return "I feed my babies milk"
