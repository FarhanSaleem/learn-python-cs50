import random


class Hat:

    def __init__(self):
        self.houses = ["Marietta", "Alpharetta", "Dunwoody", "Decatur"]

    def sort(self, name):
        print(name, "is in", random.choice(self.houses))


hat = Hat()
hat.sort("Harry")