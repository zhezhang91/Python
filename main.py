# Global variables
import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}
playing = True


class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck():
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return 'The deck has: ' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand():
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips():
    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):

    while True:

        try:
            chips.bet = int(input('How many chips would you like to bet?'))
        except:
            print('Sorry please provide an integer')
        else:
            if chips.bet > chips.total:
                print(
                    f'Sorry, you do not have enough chips! You currently have: {chips.total}')
            else:
                break


def hit(deck, hand):
    single_card = deck.deal()
    hand.add_card()
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input('Hit or Stand? Enter h or s ')

        if x[0].lower() == 'h':
            hit(deck, hand)

        elif x[0].lower() == 's':
            print("Player Stands Dealer's Turn")
            playing = False

        else:
            print("Sorry, I did not understand that, Please enter h ro s only!")
            continue

        break


def show_some(player, dealer):  # creates a function that receives two Hand() objects as parameter
    print("\nDealer's Hand:")  # print the string
    # print the string card hidden, as if there was a card there
    print(" <card hidden>")
    print('', dealer.cards[1])  # show the second card from dealer
    # print every card inside of player.cards, separated by a new line
    print("\nPlayer's Hand:", *player.cards, sep='\n ')


def show_all(player, dealer):  # creates a function that receives two Hand() objects as parameter
    # print every card inside of dealer.cards, separated by a new line
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    # print the value from dealer's hand
    print("Dealer's Hand =", dealer.value)
    # print every card inside of player.cards, separated by a new line
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =", player.value)  # print the value for player's hand


def player_busts(player, dealer, chips):
    print('BUST PLAYER!')
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print('PLAYER WINS!')
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print('PLAYER WINS! DEALER BUSTED!')
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print('DEALER WINS! ')
    chips.lose_bet()


def push(player, dealer):
    print('Dealer and Player tie! PUSH')
