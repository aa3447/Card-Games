import unittest
from card import Card
from deck import Deck, Suits, Ranks

class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_deck_initialization(self):
        self.assertEqual(len(self.deck.cards), 52)

    def test_deal_card(self):
        card = self.deck.deal()
        self.assertIsNotNone(card)
        self.assertEqual(len(self.deck.cards), 51)

    def test_deal_all_cards_with_correct_ranks_and_suits(self):
        dealt_cards = []
        for _ in range(52):
            dealt_cards.append(self.deck.deal())

        for suit in Suits:
            for rank in Ranks:
                self.assertIn(Card(suit, rank), dealt_cards)
        
        card = self.deck.deal()
        self.assertIsNone(card)


if __name__ == "__main__":
    unittest.main()