from card import Card, Suits, Ranks
from enum import Enum
from random import shuffle

class Deck:
    def __init__(self, custom_ranks = Ranks):
        self.cards: list[Card] = []
        for suit in Suits:
            for rank in custom_ranks:
                self.cards.append(Card(suit, rank))

    def deal(self) -> Card:
        if len(self.cards) == 0:
            return None
        return self.cards.pop()
    
    def multi_deal(self, num_cards) -> list[Card]:
        cards = []
        if len(self.cards) < num_cards:
            return None
        for _ in range(num_cards):
            cards.append(self.cards.pop())
        return cards
    
    def shuffle(self):
        shuffle(self.cards)
    
    def refill(self):
        self.cards = []
        for suit in Suits:
            for rank in Ranks:
                self.cards.append(Card(suit, rank))

    def get_cards_remaining(self) -> int:
        return len(self.cards)
    
    def is_empty(self) -> bool:
        return len(self.cards) == 0
        
        