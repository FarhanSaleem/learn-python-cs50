# imports the whole random module
# import random
# import the function explicitly from the module


# from random import choice

# coin = choice(["heads","tails"])
# print(coin)

import random

cards = ["joker","queen","king"]
random.shuffle(cards)

for card in cards:
    print(card)