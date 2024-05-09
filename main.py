import random

suits: list[str] = ['Spade', 'Club', 'Heart', 'Diamond']
ranks: list[str] = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank


class Game:
    def __init__(self):
        self.deck: list[Card] = list()
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
        random.shuffle(self.deck)

        self.players = {
            "Player 1": [],
            "Player 2": []
        }

        for i in range(10):
            self.players["Player 1"].append(self.deck.pop())
            self.players["Player 2"].append(self.deck.pop())

    def _show_cards(self):
        for player_name, player_cards in self.players.items():
            print(f"\n{player_name}'s Cards: ")
            for card in player_cards:
                print(card.suit, card.rank)


if __name__ == "__main__":
    game = Game()
    print('DEBUG: Game initialized')
