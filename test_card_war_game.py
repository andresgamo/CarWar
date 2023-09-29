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
        self.assertEqual(str(self.deck.cards[0]), "2♣")
        self.assertEqual(str(self.deck.cards[-1]), "A♠")

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


class testPlayer(unittest.TestCase):
    def setUp(self):
        self.hand = [Card("A", "♠"), Card("2", "♣"), Card("3", "♦"), Card("4", "♥")]
        self.player = Player("user_test", self.hand)

    def test_init(self):
        """Test initialization attributes"""
        self.assertEqual(self.player.name, "user_test")
        self.assertEqual(self.player.cards, self.hand)

    def test_len(self):
        """Test __len__ method"""
        self.assertEqual(len(self.player), 4)

    def test_str(self):
        """Test __str__ method"""
        self.assertEqual(str(self.player), "User_test has 4 cards.")

    def test_bet(self):
        """Test bet method"""
        top_card = self.hand[0]
        self.assertEqual(self.player.bet(), top_card)

    def test_add_cards(self):
        """Test add_cards method"""
        pit = [Card("5", "♠")]
        self.player.add_cards(pit)
        self.assertEqual(len(self.player), 5)
        self.assertEqual(self.player.cards[-1], pit[0])


if __name__ == "__main__":
    unittest.main()
