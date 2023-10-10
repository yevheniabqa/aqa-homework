from mammal import Mammal


# Define 'Monkey' is a child class of 'Mammal'
class Monkey(Mammal):
    def __init__(self, name, species, fur_color, tail_length):
        super().__init__(name, species, fur_color)
        self.tail_length = tail_length

    def speak(self):
        return "I'm a monkey, I hoot and screech"

    def swing_from_branch(self):
        return "I'm swinging om branches!"

