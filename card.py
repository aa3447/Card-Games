from enum import Enum

class Colors(Enum):
    RED = 1
    BLACK = 2

class Card:
    def __init__(self,suit, rank):
        self.suit = suit
        self.rank = rank
        if suit == "Hearts" or suit == "Diamonds":
            self.color = Colors.RED
        else:
            self.color = Colors.BLACK
        self._value = rank
        self._is_flipped = False
    
    def get_suit(self):
        return self.suit
    
    def get_rank(self):
        return self.rank
    
    def get_value(self):
        return self._value
    
    def get_color(self):
        return self.color
    
    def set_value(self, value):
        self._value = value

    def flip(self):
        self._is_flipped = not self._is_flipped
    
    def is_flipped(self):
        return self._is_flipped
    
    def __eq__(self, other):
        if isinstance(other, Card):
            return self.suit == other.suit and self.rank == other.rank
        return False
    
    def __str__(self):
        return f"{self.rank.name} of {self.suit.name}"
    
    def __repr__(self):
        return f"Card({self.suit}, {self.rank})"