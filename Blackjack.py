import Cards
import random

face_card_values = {11: 10, 12: 10, 13: 10}  # Blackjack face card values should all equal 10
player_balance = 1000  # Initial balance for player


# Function to deal a card to a hand (player or dealer)
def Hit(turn):
    card = random.choice(Cards.deck)
    turn.append(card)
    Cards.deck.remove(card)
    return card


# Function to deal initial cards to the player and the dealer
def Deal():
    for _ in range(2):
        Hit(PlayerHand)
        Hit(DealerHand)


def Total(turn):  # Calculates total of hand including identifying value of ace
    total = 0
    num_aces = 0

    for card in turn:
        card_value = card.value
        if card_value in face_card_values:
            total += face_card_values[card_value]
        else:
            total += card_value
        if card_value == 1:
            num_aces += 1
    while total + 10 <= 21 and num_aces > 0:
        total += 10
        num_aces -= 1

    return total


print("Welcome to BlackJack!")
print("Player Balance: $", player_balance)

while True:  # Start of game replay loop
    random.shuffle(Cards.deck)
    PlayerHand = []
    DealerHand = []

    bet = int(input("Place Your Bets: $ "))
    player_balance -= bet
    print("New Player Balance: $", player_balance)

    print("\nDealing Cards...")
    Deal()

    player_cards_str = ", ".join(str(card) for card in PlayerHand)
    dealer_cards_str = ", ".join(str(card) for card in DealerHand)
    print("Player's Hand: ", player_cards_str)
    print("Dealer's Hand: ", DealerHand[0], "\n")

    while True:  # Start of player loop
        print("Your hands total value is: ", Total(PlayerHand))
        if Total(PlayerHand) > 21:
            print("Player Busted!\n\nDealer's Turn...")
            break
        else:
            player = input("Would you like another card? (Y/N): ")

            while player.upper() not in ["Y", "N"]:
                print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")
                player = input("Would you like another card? (Y/N): ")

            if player.upper() == "Y":
                Hit(PlayerHand)
                player_cards_str = ", ".join(str(card) for card in PlayerHand)
                print("\nPlayer's Hand: ", player_cards_str)
            else:
                print("\nDealer's Turn...")
                break

    print("Dealer's Hand: ", dealer_cards_str)
    print("Dealer's Total: ", Total(DealerHand))

    while Total(DealerHand) < 17:  # Start of dealer loop
        Hit(DealerHand)
        dealer_cards_str = ", ".join(str(card) for card in DealerHand)
        print("\nDealer's Hand: ", dealer_cards_str)
        print("Dealer's Total: ", Total(DealerHand))
        if Total(DealerHand) > 21:
            print("Dealer Busted!")

    player_total = Total(PlayerHand)
    dealer_total = Total(DealerHand)

    print("\nPlayer's Total: ", player_total)
    print("Dealer's Total: ", dealer_total)

    if player_total > 21:
        print("\nPlayer Busted! Dealer Wins!")
    elif dealer_total > 21:
        print("\nDealer Busted! Player Wins! You Won ", bet * 2)
        player_balance += bet * 2
    elif player_total > dealer_total:
        print("\nPlayer Wins! You Won ", bet * 2)
        player_balance += bet * 2
    elif player_total < dealer_total:
        print("\nDealer Wins!")
    else:
        print("\nIt's a Tie!")
        player_balance += bet
    # Decides victor and loser and bet winnings

    print("\nPlayer Balance: $", player_balance)

    if player_balance == 0:
        print("You have nothing left to bet!\nThanks For Playing! Goodbye!")
        break

    play_again = input("Do you want to play again? (Y/N): ")

    while play_again.upper() not in ["Y", "N"]:
        print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")
        play_again = input("Do you want to play again? (Y/N): ")

    if play_again.upper() == "Y":
        print("\nLet's Go Again!")
    elif play_again.upper() == "N":
        print("\nThanks For Playing! Goodbye!")
        break
