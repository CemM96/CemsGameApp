# Define a class named Card
class Card:
    # Class-level variables for card suits and face cards
    suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
    face_cards = {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"}

    # Constructor method to initialize a card object with a value and a suit
    def __init__(self, value, suit):  #
        self.value = value
        self.suit = suit

    # Method to get the numeric or face value of the card
    # Allows customization of face card values through the face_card_values parameter
    def get_numeric_value(self, face_card_values=None):
        # If face_card_values is not provided, use the default face card values
        if face_card_values is None:
            face_card_values = {11: "Jack", 12: "Queen", 13: "King"}
        # If the card is a face card, return its corresponding name from the provided or default values
        if self.value in self.face_cards:
            return face_card_values.get(self.value, self.face_cards[self.value])

    # Method to provide a readable representation of the card
    def __repr__(self):
        # Get the name of the face card if applicable, otherwise display the numeric value
        face_card_name = self.face_cards.get(self.value)
        if face_card_name:
            return f"{face_card_name} of {self.suit}"
        return f"{self.value} of {self.suit}"


# Create a deck of cards by generating card objects for all combinations of suits and values
deck = [Card(value, suit) for suit in Card.suits for value in range(1, 14)]
