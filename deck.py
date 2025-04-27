from card import Card
from enum import Enum
from random import shuffle

class Suits(Enum):
    HEARTS = 1
    DIAMONDS = 2
    CLUBS = 3
    SPADES = 4

class Ranks(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13

class Deck:
    def __init__(self):
        self.cards = []
        for suit in Suits:
            for rank in Ranks:
                self.cards.append(Card(suit, rank))

    def deal(self):
        if len(self.cards) == 0:
            print("No cards left in the deck.")
            return None
        return self.cards.pop()
    
    def shuffle(self):
        shuffle(self.cards)
        print("Deck shuffled")