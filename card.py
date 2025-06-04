from enum import Enum

class Colors(Enum):
    RED = 1
    BLACK = 2

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

class Card:
    def __init__(self,suit, rank):
        self.suit = suit
        self.rank = rank
        if self.suit == Suits.HEARTS or self.suit == Suits.DIAMONDS:
            self.color = Colors.RED
        else:
            self.color = Colors.BLACK
        self._value = rank
        self._is_flipped: bool = False
        self._image_path = ""
    
    def get_suit(self):
        return self.suit
    
    def get_rank(self):
        return self.rank
    
    def get_value(self):
        return self._value
    
    def get_color(self):
        return self.color
    
    def get_image_path(self):
        return self._image_path
    
    def set_image_path(self, path):
        self._image_path = path
    
    def set_value(self, value):
        self._value = value

    def flip(self):
        self._is_flipped = not self._is_flipped
    
    def is_flipped(self) -> bool:
        return self._is_flipped
    
    def __eq__(self, other):
        if isinstance(other, Card):
            return self.suit == other.suit and self.rank == other.rank
        return False
    
    def __str__(self):
        return f"{self.rank.name} of {self.suit.name}"
    
    def __repr__(self):
        return f"Card({self.suit}, {self.rank})"