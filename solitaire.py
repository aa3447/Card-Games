from deck import Deck
from card import Card
class Solitaire:
    def __init__(self):
        self._stock: Deck = Deck()
        self._stock.shuffle()
        self._tableau: list[list[Card]] = [[] for _ in range(7)]
        self._foundation: list[list[Card]] = [[] for _ in range(4)]
        self._waste: list[Card] = []

    def play(self):
        self._setup()
        while True:
            print("1. Draw from stock")
            print("2. Move tableau card")
            print("3. Move multiple tableau cards")
            print("4. Move from tableau to foundation")
            print("5. Move from waste to tableau")
            print("6. Move from waste to foundation")   
            print("7. Show all useable cards")
            print("8. Show columns")
            print("9. Show foundations")
            print("10. Show waste")
            print("11. Quit")
            choice = input("Enter your choice: ")
            
            match choice:
                case "1":
                    self._draw_from_stock()
                case "2":
                    from_column = int(input("Enter the column to move from (0-6): "))
                    to_column = int(input("Enter the column to move to (0-6): "))
                    self._move_card(from_column, to_column)
                case "3":
                    from_column = int(input("Enter the column to move from (0-6): "))
                    to_column = int(input("Enter the column to move to (0-6): "))
                    num_cards = int(input("Enter the number of cards to move: "))
                    self._move_multiple_cards(from_column, to_column, num_cards)
                case "4":
                    from_column = int(input("Enter the column to move from (0-6): "))
                    foundation = int(input("Enter the foundation to move to (0-3): "))
                    self._move_card_to_foundation(from_column, foundation)
                case "5":
                    tableau_column = int(input("Enter the tableau column to move from (0-6): "))
                    self._move_card_from_waste_to_tableau(tableau_column)
                case "6":
                    foundation = int(input("Enter the foundation to move to (0-3): "))
                    self._move_card_from_waste_to_foundation(foundation)
                case "7":
                    self._show_all_useable_cards()
                case "8":
                    column = int(input("Enter the column number (0-6): "))
                    self._show_column_by_index(column)
                case "9":
                    foundation = int(input("Enter the foundation number (0-3): "))
                    self._show_foundation_by_index(foundation)
                case "10":
                    self._show_waste()
                case "11":
                    break
                case _:
                    print("Invalid choice")

    def _setup(self):
        for i in range(7):
            for j in range(i, 7):
                self._tableau[j].append(self._stock.deal())
        for column in self._tableau:
            column[-1].flip()
        waste_card = self._stock.deal()
        waste_card.flip()
        self._waste.append(waste_card)
    
    def _move_card(self, from_column: int, to_column: int):
        if not self._tableau[from_column][-1].is_flipped() or not self._tableau[to_column][-1].is_flipped():
            print("You cannot move a card to or from a face down card")
            return
        if from_column < 0 or from_column > 6 or to_column < 0 or to_column > 6:
            print("Invalid column number")
            return
        if from_column == to_column:
            print("You cannot move a card to the same column")
            return
        if not self._tableau[from_column]:
            print("You cannot move a card from an empty tableau column")
            return
        
        card = self._tableau[from_column][-1]
        if self._insert_into_tableau(card, to_column):
            self._tableau[from_column].pop()
            if not self._tableau[from_column][-1].is_flipped():
                self._tableau[from_column][-1].flip()
        else:
            print("You can only place a card on a tableau column if it is the opposite color and one rank lower")

    def _move_card_to_foundation(self, from_column: int, foundation: int):
        if not self._tableau[from_column][-1].is_flipped():
            print("You cannot move a card to or from a face down card")
            return
        if from_column < 0 or from_column > 6 or foundation < 0 or foundation > 3:
            print("Invalid column number")
            return
        if not self._tableau[from_column]:
            print("You cannot move a card from an empty tableau column")
            return
        
        card = self._tableau[from_column][-1]
        if self._insert_into_foundation(card, foundation):
            self._tableau[from_column].pop()
            if not self._tableau[from_column][-1].is_flipped():
                self._tableau[from_column][-1].flip()
        else:
            print("You can only place a card on a foundation if it is the same suit and one rank higher")
    
    def _move_card_from_waste_to_foundation(self, foundation: int):
        if not self._waste[-1].is_flipped():
            print("You cannot move a card to or from a face down card")
            return
        if foundation < 0 or foundation > 3:
            print("Invalid foundation number")
            return
        if not self._waste:
            print("You cannot move a card from an empty waste pile")
            return
        
        card = self._waste[-1]
        if self._insert_into_foundation(card, foundation):
            self._waste.pop()
        else:
            print("You can only place a card on a foundation if it is the same suit and one rank higher")
    
    def _move_card_from_waste_to_tableau(self, column: int):
        if not self._waste[-1].is_flipped():
            print("You cannot move a card to or from a face down card")
            return
        if column < 0 or column > 6:
            print("Invalid column number")
            return
        if not self._waste:
            print("You cannot move a card from an empty waste pile")
            return
        
        card = self._waste[-1]
        if self._insert_into_tableau(card, column):
            self._waste.pop()
        else:
            print("You can only place a card on a tableau column if it is the opposite color and one rank lower")

    def _move_multiple_cards(self, from_column: int, to_column: int, num_cards: int):
        if not self._tableau[from_column][-1].is_flipped() or not self._tableau[to_column][-1].is_flipped():
            print("You cannot move a card to or from a face down card")
            return
        if from_column < 0 or from_column > 6 or to_column < 0 or to_column > 6:
            print("Invalid column number")
            return
        if from_column == to_column:
            print("You cannot move a card to the same column")
            return
        if not self._tableau[from_column]:
            print("You cannot move a card from an empty tableau column")
            return
        if num_cards > len(self._tableau[from_column]):
            print("You cannot move more cards than are in the column")
            return
        if num_cards < 1:
            print("You must move at least one card")
            return
        if not self._tableau[from_column][-num_cards].is_flipped():
            print("You cannot move a card to or from a face down card")
            return
        
        cards = self._tableau[from_column][-num_cards:]
        if self._insert_multiple_into_tableau(cards, to_column):
            for _ in range(num_cards):
                self._tableau[from_column].pop()
        else:
            print("You can only place a card on a tableau column if it is the opposite color and one rank lower")
    
    def _insert_into_foundation(self, card: Card, foundation: int) -> bool:
        if foundation < 0 or foundation > 3:
            print("Invalid foundation number")
            return False
        

        if not self._foundation[foundation]:
            if card.get_rank().value == 1:
                self._foundation[foundation].append(card)
            else:
                print("You can only place a card on an empty foundation if it is an Ace")
                return False
        else:
            top_card = self._foundation[foundation][-1]
            if card.get_suit() == top_card.get_suit() and card.get_rank().value == top_card.get_rank().value + 1:
                self._foundation[foundation].append(card)
            else:
                print("You can only place a card on a foundation if it is the same suit and one rank higher")
                return False
        return True
    
    # Assumses cards are in the correct order
    def _insert_multiple_into_foundation(self, cards: list[Card], foundation: int) -> bool:
        if foundation < 0 or foundation > 3:
            print("Invalid foundation number")
            return False

        if not self._foundation[foundation]:
            if cards[0].get_rank().value == 1:
                self._foundation[foundation].extend(cards)
            else:
                print("You can only place a card on an empty foundation if it is an Ace")
                return False
        else:
            top_card = self._foundation[foundation][-1]
            if cards[0].get_suit() == top_card.get_suit() and cards[0].get_rank().value == top_card.get_rank().value + 1:
                self._foundation[foundation].extend(cards)
            else:
                print("You can only place a card on a foundation if it is the same suit and one rank higher")
                return False
        return True
    
    def _insert_into_tableau(self, card: Card, column: int) -> bool:
        if column < 0 or column > 6:
            print("Invalid column number")
            return False

        if not self._tableau[column]:
            if card.get_rank().value == 13:
                self._tableau[column].append(card)
            else:
                print("You can only place a King on an empty tableau column")
                return False
        else:
            top_card = self._tableau[column][-1]
            if card.get_color() != top_card.get_color() and card.get_rank().value == top_card.get_rank().value - 1:
                self._tableau[column].append(card)
            else:
                print("You can only place a card on a tableau column if it is the opposite color and one rank lower")
                return False
        return True
    
    # Assumses cards are in the correct order
    def _insert_multiple_into_tableau(self, cards: list[Card], column: int) -> bool:
        if column < 0 or column > 6:
            print("Invalid column number")
            return False

        if not self._tableau[column]:
            if cards[0].get_rank().value == 13:
                self._tableau[column].extend(cards)
            else:
                print("You can only place a King on an empty tableau column")
                return False
        else:
            top_card = self._tableau[column][-1]
            if cards[0].get_color() != top_card.get_color() and cards[0].get_rank().value == top_card.get_rank().value - 1:
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
    
    def _show_column_by_index(self, column_index: int):
        if column_index < 0 or column_index > 6:
            print("Invalid column number")
            return

        cards = ""
        print("Cards in colomun from top to bottom")
        for card in self._tableau[column_index]:
            if card.is_flipped():
                cards += str(card) + " " + str(card.get_color().name) + " "
        print(cards)

    def _show_column(self, column: list[Card], index: int = 0):

        cards = ""
        print(f"Cards in colomun {index} from top to bottom")
        for card in column:
            if card.is_flipped():
                cards += str(card) + " " + str(card.get_color().name) + " "
        print(cards)
    
    def _show_columns(self):
        print("Colomun from left to right")
        index:int = 0
        for column in self._tableau:
            if column:
                self._show_column(column, index)
            else:
                print("Empty Column")
            index += 1

    def _show_foundation_by_index(self, foundation_index: int):
        if foundation_index < 0 or foundation_index > 3:
            print("Invalid foundation number")
            return
        
        card: Card = self._foundation[foundation_index][-1]
        print("Top card of foundation")
        print(str(card)+ " " + str(card.get_color().name))

    def _show_foundation(self, foundation: list[Card], index:int = 0):
        card:Card = foundation[-1] 
        print(f"Top card of foundation {index}")
        print(str(card) + " " + str(card.get_color().name))
    
    def _show_foundations(self):
        print("Foundations from left to right")
        index: int = 0
        for foundation in self._foundation:
            if not foundation:
                print("Empty Foundation")
            else:
                self._show_foundation(foundation, index)
            index += 1
    
    def _show_waste(self):
        card:Card = self._waste[-1]
        print("Waste card")
        print(str(card) + " " + str(card.get_color().name))
                
            