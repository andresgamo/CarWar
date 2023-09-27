import unittest
from car_war_game import Card, Deck, Player, Game


class testCard(unittest.TestCase):
    def setUp(self):
        """Instansiate test case"""
        self.card = Card("A", "♠")

    def test_card_init(self):
        """Test initialization attributes"""
        self.assertIsNotNone(self.card)
        self.assertEqual(self.card.rank, "A")
        self.assertEqual(self.card.suit, "♠")
        self.assertEqual(self.card.value, 14)

    def test_card_str(self):
        """Test __str__ method"""
        self.assertEqual(str(self.card), "A♠")


if __name__ == "__main__":
    unittest.main()
