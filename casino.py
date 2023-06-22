import random

class Deck(object):
    def __init__(self):
        suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
        ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(rank + " of " + suit)


    def shuffle(self):
        random.shuffle(self.cards)

    def giveDeck(self):
        return self.cards

    def dealCard(self):
        return self.cards.pop()


class Dice(object):
    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper

    def roll(self):
        return random.randint(self.lower, self.upper)
