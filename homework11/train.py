from custom_iterator import CustomIterator
import random

class Passenger:
    def __init__(self, name):
        self.name = name


class Wagon:
    def __init__(self, number):
        self.number = number
        self.passengers = []

    def add_passenger(self, passenger):
        if len(self.passengers) < 10:
            self.passengers.append(passenger)
        else:
            print(f"Wagon {self.number} is already full, cannot add more passengers!")

    def __len__(self):
        return len(self.passengers)

    def __str__(self):
        return f"[{self.number}]"


class Train:
    def __init__(self):
        self.wagons = []

    def add_wagon(self, wagon):
        self.wagons.append(wagon)

    def __len__(self):
        return len(self.wagons)

    def __str__(self):
        wagons_string = '-'.join(map(str, CustomIterator(self.wagons, 0, len(self.wagons) - 1)))
        return f"<=[HEAD]-{wagons_string}"


# Create a train and add wagons to it
train = Train()


for wagon_number in range(1, 8):
    wagon = Wagon(wagon_number)
    for passenger in range(1, random.randint(1, 13)):
        wagon.add_passenger(Passenger(name=f'don{passenger}'))
    train.add_wagon(wagon)

# Print the train
for wagon in train.wagons:
    print(f"Wagon {wagon.number}: {len(wagon)} passengers")

print(train)
