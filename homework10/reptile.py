from animal import Animal


# Define 'Reptile' is a child class of 'Animal'
class Reptile(Animal):
    def __init__(self, name, species, scale_color):
        super().__init__(name, species)
        self.scale_color = scale_color

    def speak(self):
        return "I'm reptile, I hiss and make various noises"

    def hiss(self):
        return "Hsss!"
