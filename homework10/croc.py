from reptile import Reptile

# Define 'Crocodile' is a child class of 'Reptile'
class Crocodile(Reptile):
    def __init__(self, name, species, scale_color, size):
        super().__init__(name, species, scale_color)
        self.size = size

    def speak(self):
        return "I roar as crocodile"

    def swim(self):
        return "I swim in a swamp"
