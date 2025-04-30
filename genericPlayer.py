class Player:
    def __init__(self, name = "player"):
        self.name = name
        self.list = []
        self._chips = 0
        self._bet = 0

    def add_card(self, card):
        self.list.append(card)

    def remove_card(self):
        return self.list.pop()

    def has_cards(self):
        return len(self.list) > 0

    def get_list_size(self):
        return len(self.list)
    
    def set_chips(self, chips):
        self._chips = chips

    def get_chips(self):
        return self._chips
    
    def show_cards(self):
        hand = ""
        for card in self.list:
            hand += f"{card}, "
        print(hand)
