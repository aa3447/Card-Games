class Player:
    def __init__(self, name = "player"):
        self.name = name
        self.list = []
        self._chips = 0
        self._bet = 0
        self._has_busted = False

    def add_card(self, card):
        self.list.append(card)

    def add_cards(self, cards):
        for card in cards:
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
    
    def set_bet(self, bet):
        if bet > self._chips:
            raise ValueError("Bet exceeds available chips.")
        self._bet = bet
    
    def get_bet(self):
        return self._bet
    
    def get_cards(self):
        return self.list
    
    def set_busted(self, busted):
        self._has_busted = busted
    
    def has_busted(self):
        return self._has_busted
    
    def print_hand(self):
        hand = ""
        for card in self.list:
            hand += f"{card}, "
        return hand
