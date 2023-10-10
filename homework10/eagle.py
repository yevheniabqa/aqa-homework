from bird import Bird


# Define 'Eagle' is a child class of 'Bird'
class Eagle(Bird):
    def __init__(self, name, species, feather_color, wingspan):
        super().__init__(name, species, feather_color)
        self.wingspan = wingspan

    def speak(self):
        return"I screech loudly"

    def hunt(self):
        return "I am a sky hunter"
