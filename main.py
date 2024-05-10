import random

suits: list[str] = ['Spade', 'Club', 'Heart', 'Diamond']
ranks: list[str] = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.flipped = False

    def flip(self):
        self.flipped = not self.flipped


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

    def show_cards(self):
        for player_name, player_cards in self.players.items():
            print(f"\n{player_name}'s Cards: ")
            print_str = str()
            itr: int = 0
            for card in player_cards:
                if not card.flipped:
                    print_str += "[X] "
                else:
                    print_str += f"[{card.rank}] "
                # Each card is laid out in rows of 5 for each player.
                if itr == 4:
                    print_str += "\n"
                itr += 1
            print(print_str)


if __name__ == "__main__":
    game = Game()
    print('DEBUG: Game initialized')
    game.show_cards()
