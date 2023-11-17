import Cards
import random

face_card_values = {11: 10, 12: 10, 13: 10}  # Blackjack face card values should all equal 10


# Function to deal a card to a hand (player or dealer)
def hit(turn):
    card = random.choice(Cards.deck)
    turn.append(card)
    Cards.deck.remove(card)
    return card


# Function to deal initial cards to the player and the dealer
def deal(player_hand, dealer_hand):
    for _ in range(2):
        hit(player_hand)
        hit(dealer_hand)


# Function to calculate the total value of a hand and handle aces
def calculate_total(turn):
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


def game_loop(player_balance):
    # Print welcome message and initial player balance
    print("Welcome to BlackJack!")
    print("Player Balance: $", player_balance)
    # Main game loop
    while True:
        random.shuffle(Cards.deck)
        player_hand = []
        dealer_hand = []

        bet = int(input("Place Your Bets: $ "))
        player_balance -= bet
        print("New Player Balance: $", player_balance)

        print("\nDealing Cards...")
        deal(player_hand, dealer_hand)

        player_cards_str = ", ".join(str(card) for card in player_hand)
        dealer_cards_str = ", ".join(str(card) for card in dealer_hand)
        print("Player's Hand: ", player_cards_str)
        print("Dealer's Hand: ", dealer_hand[0], "\n")

        # Start of player loop
        while True:
            print("Your hands total value is: ", calculate_total(player_hand))
            if calculate_total(player_hand) > 21:
                print("Player Busted!\n\nDealer's Turn...")
                break
            else:
                player = input("Would you like another card? (Y/N): ")

                while player.upper() not in ["Y", "N"]:
                    print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")
                    player = input("Would you like another card? (Y/N): ")

                if player.upper() == "Y":
                    hit(player_hand)
                    player_cards_str = ", ".join(str(card) for card in player_hand)
                    print("\nPlayer's Hand: ", player_cards_str)
                else:
                    print("\nDealer's Turn...")
                    break

        print("Dealer's Hand: ", dealer_cards_str)
        print("Dealer's Total: ", calculate_total(dealer_hand))

        # Start of dealer loop
        while calculate_total(dealer_hand) < 17:
            hit(dealer_hand)
            dealer_cards_str = ", ".join(str(card) for card in dealer_hand)
            print("\nDealer's Hand: ", dealer_cards_str)
            print("Dealer's Total: ", calculate_total(dealer_hand))
            if calculate_total(dealer_hand) > 21:
                print("Dealer Busted!")

        player_total = calculate_total(player_hand)
        dealer_total = calculate_total(dealer_hand)

        print("\nPlayer's Total: ", player_total)
        print("Dealer's Total: ", dealer_total)

        # Determine the winner and handle bets
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

        print("\nPlayer Balance: $", player_balance)

        # Check if player has no money left to bet
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


player_balance = 1000


def main():
    game_loop(player_balance)


if __name__ == "__main__":
    main()
