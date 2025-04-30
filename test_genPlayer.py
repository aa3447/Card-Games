from genericPlayer import Player
from card import Card

class TestPlayer:
    def test_player_initialization(self):
        player = Player("TestPlayer")
        assert player.name == "TestPlayer"
        assert player.list == []
        assert player.chips == 0

    def test_add_card(self):
        player = Player("TestPlayer")
        player.add_card(Card("Spades", "Ace"))
        assert player.list == [Card("Spades", "Ace")]

    def test_remove_card(self):
        player = Player("TestPlayer")
        player.add_card(Card("Spades", "Ace"))
        removed_card = player.remove_card()
        assert removed_card == Card("Spades", "Ace")
        assert player.list == []

    def test_has_cards(self):
        player = Player("TestPlayer")
        assert not player.has_cards()
        player.add_card(Card("Spades", "Ace"))
        assert player.has_cards()

    def test_get_list_size(self):
        player = Player("TestPlayer")
        assert player.get_list_size() == 0
        player.add_card(Card("Spades", "Ace"))
        assert player.get_list_size() == 1
    
    def test_chips(self):
        player = Player("TestPlayer")
        player.set_chips(100)
        assert player.get_chips() == 100