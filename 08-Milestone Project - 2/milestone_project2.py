import random


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    SUITS = ("Hearts", "Diamonds", "Spades", "Clubs")
    RANKS = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")

    def __init__(self):
        self.deck = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                self.deck.append(Card(suit, rank))

    def __repr__(self):
        empty_string = ", ".join([str(card) for card in self.deck])
        return f"[{empty_string}]"

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

class Hand:
    values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10,
              "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += self.values[card.rank]
        if card.rank == "Ace":
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

    def is_busted(self):
        return self.value > 21

class Chips:

    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

    def take_bet(self):
        while True:
            try:
                self.bet = int(input("How many chips would you like to bet? "))
            except:
                raise ValueError("Sorry, a bet must be an integer!")
            else:
                if self.bet > self.total:
                    print("Sorry, your bet can't exceed", self.total)
                else:
                    break

class Game:

    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()

        self.player_hand = Hand()
        self.player_hand.add_card(self.deck.deal())
        self.player_hand.add_card(self.deck.deal())

        self.dealer_hand = Hand()
        self.dealer_hand.add_card(self.deck.deal())
        self.dealer_hand.add_card(self.deck.deal())

    def show_some(self):
        print("\nDealer's Hand:")
        print(" <card hidden>")
        print("", self.dealer_hand.cards[1])
        print("\nPlayer's Hand:", *self.player_hand.cards, sep="\n ")

    def hit_or_stand(self):
        player_action = wait_for_input("Would you like to Hit or Stand? Enter 'h' or 's' ", str, 'hs')

        if player_action == "h":
            self.hit()
            return True

        if player_action == "s":
            print("Player stands. Dealer is playing.")
            return False

    def hit(self):
        self.player_hand.add_card(self.deck.deal())
        self.player_hand.adjust_for_ace()


def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)

def player_busts(player, dealer, chips):
    print("Player busts!")
    chips.lose_bet()

def  player_wins(player, dealer, chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print("Dealer busts!")
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print("Dealer wins!")
    chips.lose_bet()

def push(player, dealer):
    print("Dealer and Player tie! It's a push.")


def wait_for_input(message, expected_type, expected_values, error_message="Sorry, please try again."):
    while True:
        try:
            raw_value = input(message)
            value = expected_type(raw_value)
            if value not in expected_values:
                raise ValueError("Unexpected value")
            return value
        except ValueError:
            print(error_message)


def main():
    player_chips = Chips()

    while True:
        print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
        Dealer hits until she reaches 17. Aces count as 1 or 11.')

        game = Game()

        player_chips.take_bet()
        game.show_some()

        playing = True
        while playing:
            playing = game.hit_or_stand()
            game.show_some()
            if game.player_hand.is_busted():
                player_busts(game.player_hand, game.dealer_hand, player_chips)
                break

        if game.player_hand.value <= 21:
            while game.dealer_hand.value < 17:
                game.hit()
            show_all(game.player_hand, game.dealer_hand)
            if game.dealer_hand.is_busted():
                dealer_busts(game.player_hand, game.dealer_hand, player_chips)
            elif game.dealer_hand.value > game.player_hand.value:
                dealer_wins(game.player_hand, game.dealer_hand, player_chips)
            elif game.dealer_hand.value < game.player_hand.value:
                player_wins(game.player_hand, game.dealer_hand, player_chips)
            else:
                push(game.player_hand, game.dealer_hand)

        print("\nPlayer's winnings stand at", player_chips.total)

        new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
        if new_game[0].lower() == 'y':
            continue
        else:
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
