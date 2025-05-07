from deck import Deck

class Solitaire:
    def __init__(self):
        self._stock = Deck()
        self._stock.shuffle()
        self._tableau = [[] for _ in range(7)]
        self._foundation = [[] for _ in range(4)]
        self._waste = []

    def play(self):
        pass

    def _setup(self):
        for i in range(7):
            for j in range(i, 7):
                self._tableau[j].append(self._stock.deal())
        for column in self._tableau:
            column[-1].flip()
        self._waste.append(self._stock.deal())
    
    def _move_card(self, from_column, to_column):
        if not self._tableau[from_column]:
            print("You cannot move a card from an empty tableau column")
            return
        card = self._tableau[from_column][-1]
        if self._insert_into_tableau(card, to_column):
            self._tableau[from_column].pop()
        else:
            print("You can only place a card on a tableau column if it is the opposite color and one rank lower")
    
    def _move_multiple_cards(self, from_column, to_column, num_cards):
        if not self._tableau[from_column]:
            print("You cannot move a card from an empty tableau column")
            return
        cards = self._tableau[from_column][-num_cards:]
        if self._insert_multiple_into_tableau(cards, to_column):
            for _ in range(num_cards):
                self._tableau[from_column].pop()
        else:
            print("You can only place a card on a tableau column if it is the opposite color and one rank lower")
    
    def _insert_into_foundation(self, card, foundation):
        if not self._foundation[foundation]:
            if card.get_rank() == 1:
                self._foundation[foundation].append(card)
            else:
                print("You can only place a card on an empty foundation if it is an Ace")
                return False
        else:
            top_card = self._foundation[foundation][-1]
            if card.get_suit() == top_card.get_suit() and card.get_value() == top_card.get_value() + 1:
                self._foundation[foundation].append(card)
            else:
                print("You can only place a card on a foundation if it is the same suit and one rank higher")
                return False
        return True
    
    # Assumses cards are in the correct order
    def _insert_multiple_into_foundation(self, cards, foundation):
        if not self._foundation[foundation]:
            if cards[0].get_rank() == 1:
                self._foundation[foundation].extend(cards)
            else:
                print("You can only place a card on an empty foundation if it is an Ace")
                return False
        else:
            top_card = self._foundation[foundation][-1]
            if cards[0].get_suit() == top_card.get_suit() and cards[0].get_value() == top_card.get_value() + 1:
                self._foundation[foundation].extend(cards)
            else:
                print("You can only place a card on a foundation if it is the same suit and one rank higher")
                return False
        return True
    
    def _insert_into_tableau(self, card, column):
        if not self._tableau[column]:
            if card.get_rank() == 13:
                self._tableau[column].append(card)
            else:
                print("You can only place a King on an empty tableau column")
                return False
        else:
            top_card = self._tableau[column][-1]
            if card.get_color() != top_card.get_color() and card.get_value() == top_card.get_value() - 1:
                self._tableau[column].append(card)
            else:
                print("You can only place a card on a tableau column if it is the opposite color and one rank lower")
                return False
        return True
    
    # Assumses cards are in the correct order
    def _insert_multiple_into_tableau(self, cards, column):
        if not self._tableau[column]:
            if cards[0].get_rank() == 13:
                self._tableau[column].extend(cards)
            else:
                print("You can only place a King on an empty tableau column")
                return False
        else:
            top_card = self._tableau[column][-1]
            if cards[0].get_color() != top_card.get_color() and cards[0].get_value() == top_card.get_value() - 1:
                self._tableau[column].extend(cards)
            else:
                print("You can only place a card on a tableau column if it is the opposite color and one rank lower")
                return False
        return True
    
    def _draw_from_stock(self):
        if self._stock.is_empty():
            print("Stock is empty")
            return
        card = self._stock.deal()
        if card.is_flipped():
            self._waste.append(card)
        else:
            card.flip()
            self._waste.append(card)
    
    def _show_all_useable_cards(self):
        self._show_columns()
        self._show_foundations()
        self._show_waste()
    
    def _show_column(self, column):
        cards = ""
        print("Cards in colomun from bottom to top")
        for card in self._tableau[column]:
            if card.is_flipped():
                cards += str(card) + " "
        print(cards)
    
    def _show_columns(self):
        for column in self._tableau:
            print("Colomun from left to right")
            self._show_column(column)

    def _show_foundation(self, foundation):
        print("Top card of foundation")
        print(self._foundation[foundation][-1])
    
    def _show_foundations(self):
        for foundation in self._foundation:
            print("Foundations from left to right")
            self._show_foundation(foundation)
    
    def _show_waste(self):
        print("Waste card")
        print(self._waste[-1])
                
            