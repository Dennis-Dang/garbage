import random
import math

suits: list[str] = ['Spade', 'Club', 'Heart', 'Diamond']
ranks: list[str] = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.flipped = False

    def flip(self):
        self.flipped = not self.flipped

    def get_card(self):
        if not self.flipped:
            return "[X]"
        else:
            return [f"{self.rank}"]


class Player:
    def __init__(self, name: str, cards: list[Card]):
        self.name = name
        self.cards = cards

    def show_cards(self):
        print(f"\n{self.name}'s Cards: ")
        idx: int = 0
        print_str = str()
        for card in self.cards:
            print_str += f"{card.get_card()} "
            # Each card is laid out in rows of 5 for each player.
            if idx == 4:
                print_str += "\n"
            idx += 1
        print(print_str)


class Game:
    def __init__(self, num_players: int):
        self.deck: list[Card] = list()
        num_decks_needed: int = int()

        if num_players < 2:
            print("Sorry, at least 2 players is required for this game.")
            return
        else:
            # Limitation: math.ceil supports up to 52 bits of precision.
            # It's beyond the scope of the game, as it's impractical to serve that many players.
            num_decks_needed = math.ceil(num_players / 2)
        for i in range(num_decks_needed):
            for suit in suits:
                for rank in ranks:
                    self.deck.append(Card(suit, rank))
        random.shuffle(self.deck)

        self.turn_queue = list()
        self.players: list[Player] = []
        # 2 players
        for i in range(num_players):
            name = input(f"Enter Player {i+1}'s name: ")
            self.turn_queue.insert(0, name)

            # Deal 10 cards per player
            card_deal = []  # Temporarily holds cards for player.
            for j in range(10):
                card_deal.append(self.deck.pop())
            self.players.append(Player(name, card_deal))


if __name__ == "__main__":
    game = Game(num_players=2)
    if len(game.deck) == 0:
        pass
    else:
        print('DEBUG: Game initialized')
        for player in game.players:
            player.show_cards()
