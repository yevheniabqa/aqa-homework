from animal import Animal


# Define 'Bird' is a child class of 'Animal'
class Bird(Animal):
    def __init__(self, name, species, feather_color):
        super().__init__(name, species)
        self.feather_color = feather_color

    def speak(self):
        return "I'm a bird I tweet and screech"

    def fly(self):
        return "I can fly in the sky"
