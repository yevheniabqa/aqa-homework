from monkey import Monkey


# Define 'Capuchin' is a child class of 'Monkey'
class Capuchin(Monkey):
    def __init__(self, name, fur_color, tail_length, intelligence_level):
        super().__init__(name, "Capuchin Monkey", fur_color, tail_length)
        self.intelligence_level = intelligence_level

    def speak(self):
        return "U-u a-a"

    def perform_tricks(self):
        return "I do tricks!"
