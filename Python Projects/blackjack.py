#Black Jack
import random

def deck_of_cards():
    deck = ["11","2","3","4","5","6","7","8","9","10","10","10","10"]
    return random.choice(deck)

def Black_jack():
    deck = ["11","2","3","4","5","6","7","8","9","10","10","10","10"]
    
    player_deck = []
    player_deck.append(deck_of_cards())
    player_deck.append(deck_of_cards())

    dealer_hand = []
    dealer_hand.append(deck_of_cards())
    dealer_hand.append(deck_of_cards())

    print(f"Youre hand is {player_deck}")
    print(f"Dealer's hand is {dealer_hand[0]}")
    

    #While loop will conitunute asking for hit or stand till player inputs a correct action
    while player_action != "hit" or "stand":
        #Asks for waht the player wants to do
        player_action = str(input("Hit or Stand? "))
        player_action.lower()

        #After check on player action, check for win condition & if dealer needs to pull another card
        if player_action == "hit":
            player_deck.append(deck_of_cards())
            print(f"Youre hand is {player_deck}")
            print(f"Dealer's hand is {dealer_hand}")
        elif player_action == "stand":
            print(f"Youre hand is {player_deck}")
            print(f"Dealer's hand is {dealer_hand}")
        else:
            print("Incorrect Action was typed!")

    #Where Dealer will be cheacked on needing to pull addition Card
    print("Dealer pulls another card")
    #Check for Player Win condition

    #Adding if Player wants to play another round
    replay = input("Would you like to play again? Y or N")
    replay.lower()
    if replay == "N" or replay == "n":
        return
    