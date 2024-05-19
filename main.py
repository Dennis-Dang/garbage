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
        self.max_cards = 10

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

    # Expects a card to be drawn from the deck. Returns a card to discard to the garbage pile.
    def draw(self, card: Card) -> Card:
        pos: int = int()
        swap: Card
        print(f"It's a {card.rank} of {card.suit}s!")
        if int(input("1) Discard \n2) Swap\n> ")) == 1:
            return card
        else:
            self.show_cards()
            correct_input = False
            while not correct_input:
                choice = int(input("Which position do you want to swap with? \n"))
                # If card number matches chosen card position to swap with or
                # If the card drawn is a King
                if choice+1 == card.rank or card.rank == 'K':
                    self.cards[choice].flip()
                    self.cards.insert(choice, card)
                    return self.draw(self.cards.pop(choice+1))

                print("You can't swap with this card because the card number doesn't match the card number position.")

    #TODO Implement checkWin
    def check_win(self):
        pass


class Game:
    def __init__(self, num_players: int):
        self.deck: list[Card] = list()
        self.garbage: list[Card]= list()
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

        for i in range(num_players):
            name = input(f"Enter Player {i+1}'s name: ")
            self.turn_queue.insert(0, name)

            # Deal 10 cards per player
            card_deal = []  # Temporarily holds cards for player.
            for j in range(10):
                card_deal.append(self.deck.pop())
            self.players.append(Player(name, card_deal))

    def run(self):
        winner: list[str] = list(str())
        while len(winner) != 2:
            for player in self.players:
                self.garbage.append(player.draw(self.deck.pop()))
                # Check win condition
                if player.check_win():
                    winner += player.name
                    if len(winner) == 1:
                        print(f"{winner} has all cards filled up! Last Round!")
                    self.players.remove(player)
                    break

        if len(winner) == 1:
            print(f"The winner is: {winner[0]}")
        else:
            print(f"There seems to be a tie between: {winner}")


if __name__ == "__main__":
    game = Game(num_players=2)
    game.run()