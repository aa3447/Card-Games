from deck import Deck
from enum import Enum

class Ranks(Enum):
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
    ACE = 14

class War:
    def __init__(self):
        self.deck = Deck(custom_ranks=Ranks)
        self.deck.shuffle()
        self.player1_stack = []
        self.player2_stack = []
        self.tie_stack = []
        self.round_count = 0
        for i in range(26):
            self.player1_stack.append(self.deck.deal())
            self.player2_stack.append(self.deck.deal())

    def play(self, player1 = "player1", player2 = "player2", war_face_down_cards = 1):
        while len(self.player1_stack) > 0 and len(self.player2_stack) > 0:
            self.round_count += 1
            card1 = self.player1_stack.pop()
            card2 = self.player2_stack.pop()
            print(f"{player1} plays {card1.rank.name} of {card1.suit.name}")
            print(f"{player2} plays {card2.rank.name} of {card2.suit.name}")

            if card1.get_rank().value > card2.get_rank().value:
                print(f"{player1} wins this round")
                self.player1_stack.insert(0, card1)
                self.player1_stack.insert(0, card2)
                if len(self.tie_stack) > 0:
                    print(f"and {player1} wins the WAR! The stack of {len(self.tie_stack)} cards is yours!!")
                    for card in self.tie_stack:
                        self.player1_stack.insert(0, card)
                    self.tie_stack.clear()
            
            elif card1.get_rank().value < card2.get_rank().value:
                print(f"{player2} wins this round")
                self.player2_stack.insert(0, card1)
                self.player2_stack.insert(0, card2)
                if len(self.tie_stack) > 0:
                    print(f"and {player2} wins the WAR! The stack of {len(self.tie_stack)} cards is yours!!")
                    for card in self.tie_stack:
                        self.player2_stack.insert(0, card)
                    self.tie_stack.clear()
            
            else:
                if len(self.player1_stack) <= war_face_down_cards:
                    return f"{player1} dose not have enough cards for WAR! {player2} wins the game after {self.round_count} rounds!!"
                elif len(self.player2_stack) <= war_face_down_cards:
                    return f"{player2} dose not have enough cards for WAR! {player1} wins the game after {self.round_count} rounds!!"
                
                print("It's a tie! WAR!")
                self.tie_stack.append(card1)
                self.tie_stack.append(card2)
                
                for _ in range(war_face_down_cards):
                    self.tie_stack.append(self.player1_stack.pop())
                    self.tie_stack.append(self.player2_stack.pop())
        
        if len(self.player1_stack) == 0:
            return f"{player1} is out of cards! {player2} wins the game after {self.round_count} rounds!"
        else:
            return f"{player2} is out of cards! {player1} wins the game after {self.round_count} rounds!"