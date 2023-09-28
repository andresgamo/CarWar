import unittest
from car_war_game import Card, Deck, Player, Game


class testCard(unittest.TestCase):
    def setUp(self):
        """Instansiate test case"""
        self.card = Card("A", "♠")

    def test_card_init(self):
        """Test initialization attributes"""
        self.assertEqual(self.card.rank, "A")
        self.assertEqual(self.card.suit, "♠")
        self.assertEqual(self.card.value, 14)

    def test_card_str(self):
        """Test __str__ method"""
        self.assertEqual(str(self.card), "A♠")


class testDeck(unittest.TestCase):
    def setUp(self):
        """Instansiate test case"""
        self.deck = Deck()

    def test_deck_init(self):
        """Test initialization attributes"""
        self.assertEqual(len(self.deck.cards), 52)

    def test_deck_str(self):
        """Test __str__ method"""
        self.assertEqual(str(self.deck), "52")

    def test_deck_len(self):
        """Test __len__ method"""
        self.assertEqual(len(self.deck), 52)

    def test_shuffle(self):
        """Test shuffle method"""
        original = self.deck.cards.copy()
        self.deck.shuffle()
        self.assertNotEqual(original, self.deck.cards)

    def test_split(self):
        """Test split method"""
        hands = self.deck.split(3)
        self.assertEqual(len(hands), 3)
        self.assertTrue(all(len(hand) == 17 for hand in hands))


if __name__ == "__main__":
    unittest.main()
