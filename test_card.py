import unittest
from card import Card

class TestCard(unittest.TestCase):
    def setUp(self):
        self.card = Card("Hearts", "Ace")

    def test_get_suit(self):
        self.assertEqual(self.card.get_suit(), "Hearts")

    def test_get_rank(self):
        self.assertEqual(self.card.get_rank(), "Ace")

if __name__ == "__main__":
    unittest.main()