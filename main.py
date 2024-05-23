import random
import math
import pyinputplus

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

    # Continue swapping cards until encounter garbage card to return/discard
    def swap(self, card: Card) -> Card:
        correct_input = False
        while not correct_input:
            self.show_cards()

            if card.rank == 'Q' or card.rank == 'J':
                print(f"You got {card.rank}.. this card is garbage.")
                return card

            choice = pyinputplus.inputMenu(['Swap', 'Discard'],
                                           "Do you want to swap or discard?\n",
                                           numbered=True)

            if choice == 'Discard':
                return card
            else:
                choice = int(input(f"Which position do you want to swap {card.rank} with?  \n"))
                # If card number matches chosen card position to swap with or
                # If the card drawn is a King
                if str(choice) == card.rank or card.rank == 'K' or (choice == 1 and card.rank == 'A'):
                    if not self.cards[choice-1].flipped:
                        self.cards[choice - 1].flip()
                    print(f"The card at position {choice} was {self.cards[choice-1].rank} of {self.cards[choice-1].suit}")
                    self.cards.insert(choice, card)
                    return self.swap(self.cards.pop(choice-1))

                print("You can't swap with this card because the card number doesn't match the card number position.")

    def check_win(self):
        # If all the cards are flipped -> they win the game
        for card in self.cards:
            if not card.flipped:
                return False
        return True


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

    def draw(self, player: Player):
        if len(self.garbage) == 0:
            print("Garbage is empty, so you draw from the deck...")
            choice = 'Draw new Card'
        else:
            print(f"Garbage: {self.garbage[-1].rank}")
            choice = pyinputplus.inputMenu(['Garbage', 'Draw new Card'],
                                           "Do you want to draw from Garbage or a new card?\n",
                                           numbered=True)
        hand: Card
        if choice == 'Draw new Card':
            hand = self.deck.pop()
            hand.flip()
            print(f"It's a {hand.rank} of {hand.suit}!")
        elif choice == 'Garbage':
            hand = self.garbage.pop()

        self.garbage.append(player.swap(hand))
        print(f"Ending turn..")

    def run(self):
        winner: list[str] = list(str())
        done = False
        while len(winner) != 2 and not done:
            for player in self.players:
                print(f"It's {player.name}'s turn!")
                input("Press Enter to continue...")
                player.show_cards()
                self.draw(player)
                # Check win condition
                if player.check_win():
                    winner.append(player.name)
                    if len(winner) == 1:
                        print(f"{winner[0]} has all cards filled up! Last Round!")
                    elif len(winner) > 1:
                        done = True
                    self.players.remove(player)
                    break

        if len(winner) == 1:
            print(f"The winner is: {winner[0]}")
        else:
            print(f"There seems to be a tie between: {winner}")


if __name__ == "__main__":
    game = Game(num_players=2)
    game.run()
