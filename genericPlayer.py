from card import Card

class Player:
    def __init__(self, name = "player", player_number = 1):
        self.name = name
        self.list = []
        self._chips = 0
        self._bet = 0
        self._has_busted = False
        self._player_number = player_number

    def add_card(self, card):
        self.list.append(card)

    def add_cards(self, cards):
        for card in cards:
            self.list.append(card)

    def remove_card(self) -> Card:
        return self.list.pop()

    def has_cards(self) -> bool:
        return len(self.list) > 0
    
    def set_chips(self, chips):
        self._chips = chips
    
    def set_player_number(self, player_number):
        self._player_number = player_number

    def get_chips(self) -> int:
        return self._chips
    
    def set_bet(self, bet):
        if bet > self._chips:
            raise ValueError("Bet exceeds available chips.")
        self._bet = bet

    def get_list_size(self) -> int:
        return len(self.list)
    
    def get_bet(self):
        return self._bet
    
    def get_cards(self):
        return self.list
    
    def get_player_number(self) -> int:
        return self._player_number
    
    def set_busted(self, busted):
        self._has_busted = busted
    
    def has_busted(self) -> bool:
        return self._has_busted
    
    def print_hand(self) -> str:
        hand = ""
        for card in self.list:
            hand += f"{card}, "
        return hand
