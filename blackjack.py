import random


class Deck:
    def __init__(self) -> None:
        self.suits = ["Hearts", "Clubs", "Diamonds", "Spades"]
        self.ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                      "Jack", "Queen", "King"]
        # create a list of all cards
        self.ordered_cards = [{'suit': suit, 'rank': rank}
                              for suit in self.suits for rank in self.ranks]

        self.cards = [{'suit': suit, 'rank': rank}
                      for suit in self.suits for rank in self.ranks]

    def shuffle(self) -> None:
        # shuffle the list of cards randomly
        random.shuffle(self.cards)

    def print_deck(self) -> None:
        print(self.cards)

    def pretty_print_deck(self) -> None:
        for card in self.cards:
            print(f"{card['rank']} of {card['suit']}")

    def pretty_print_ordered_deck(self) -> None:
        for card in self.ordered_cards:
            print(f"{card['rank']} of {card['suit']}")
            if card['rank'] == self.ranks[-1]:
                print()


class BlackJack:
    def __init__(self) -> None:
        # create a deck of cards
        self.deck = Deck()
        self.deck.shuffle()

        # assign the player and dealer 2 cards each off the top of the deck
        starting_card_count = 2

        self.player_hand = self.deck.cards[:starting_card_count]
        self.deck.cards = self.deck.cards[starting_card_count:]

        self.dealer_hand = self.deck.cards[:starting_card_count]
        self.deck.cards = self.deck.cards[starting_card_count:]

    def deal(self) -> None:
        # give one card to the player off the top of the deck
        self.player_hand.append(self.deck.cards.pop(0))

    def print_player_hand(self) -> None:
        print("Your cards are:")
        for card in self.player_hand:
            print(f"  {card['rank']} of {card['suit']}")


if __name__ == "__main__":
    blackjack = BlackJack()
    # blackjack.print_player_hand()
    blackjack.deal()
    # blackjack.print_player_hand()
    blackjack.deck.pretty_print_ordered_deck()
