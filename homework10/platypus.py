from mammal import Mammal


# Define 'Platyopus' is a child class of 'Mammal'
class Platypus(Mammal):
    def __init__(self, name, species, fur_color, lays_eggs):
        super().__init__(name, species, fur_color)
        self.lays_eggs = lays_eggs

    def speak(self):
        super(Mammal, self).speak()  # call Human
        super().speak()                # super(Manager, self).think()
        return "I make grunting sounds"

    def be_weird(self):
        return "I'm wierd tho"

