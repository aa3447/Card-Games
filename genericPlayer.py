class Player:
    def __init__(self, name = "player"):
        self.name = name
        self.list = []

    def add_card(self, card):
        self.list.append(card)

    def remove_card(self):
        return self.list.pop()

    def has_cards(self):
        return len(self.list) > 0

    def get_list_size(self):
        return len(self.list)