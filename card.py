class Card:
    def __init__(self,suit, rank):
        self.suit = suit
        self.rank = rank
        self._value = rank
    
    def get_suit(self):
        return self.suit
    
    def get_rank(self):
        return self.rank
    
    def get_value(self):
        return self._value
    
    def set_value(self, value):
        self._value = value
    
    def __eq__(self, other):
        if isinstance(other, Card):
            return self.suit == other.suit and self.rank == other.rank
        return False
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"