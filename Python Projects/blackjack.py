#Black Jack Game
import random
from os import system

def deck_of_cards():
    deck = ["11","2","3","4","5","6","7","8","9","10","10","10","10"]
    return random.choice(deck)

def Black_Jack():
    
    #Players Hand
    player_deck = []
    player_deck.append(deck_of_cards())
    player_deck.append(deck_of_cards())

    #Dealers Hand
    dealer_hand = []
    dealer_hand.append(deck_of_cards())
    dealer_hand.append(deck_of_cards())

    player_total = 0
    for hand in player_deck:
        player_total += int(hand)

    #Display the players two cards and the dealers one card
    print(f"Your hand is {', '.join(player_deck)}  Your total is {player_total}")
    print(f"The dealer's hand is {dealer_hand[0]}")

    #Check if the user wants to use an Ace as a 1 or 11
    for cards in player_deck:
        if cards == "11":
            decision = ""
            print("You have an Ace")
            decision = str(input("Would you like to count he Ace as a 1 or 11? "))
            if decision == "1":
                index = player_deck.index("11")
                player_deck[index] = "1"

    #while loop will coninute till player inputs correct action
    player_action = ""
    while player_action != "stand":
        player_action = str(input("Hit or Stand? "))
        player_action = player_action.lower()
        input("Press Enter to Continue... ")
        system("cls")

        player_total = 0
        for hand in player_deck:
            player_total += int(hand)

        #Check player inputed the correct action
        if player_action == "hit":
            player_deck.append(deck_of_cards())
            print(f"You pulled a {player_deck[-1]}")
            print(f"Your hand is {', '.join(player_deck)} Your total is {player_total}")
            print(f"The dealer's hand is {dealer_hand[0]}")
        elif player_action == "stand":
            break
        else:
            print("Incorrect Action was typed")

        #Check if the user wants to use an Ace as a 1 or 11
        for cards in player_deck:
            if cards == "11":
                decision = ""
                print("You have an Ace")
                decision = str(input("Would you like to count he Ace as a 1 or 11? "))
                if decision == "1":
                    index = player_deck.index("11")
                    player_deck[index] = "1"
        system("cls")
        player_total += int(player_deck[-1])
        print(f"Your new hand is {', '.join(player_deck)} Your total is {player_total}")
        #Check the Total value of PLayers Hand

        #Chek if the Player busted
        if player_total > 21:
            player_action = "stand"


    #Dealer will be checked once all players have done their turn
    dealer_total = 0
    for hand in dealer_hand:
        dealer_total += int(hand)

    #calculate the player's hand
    player_total = 0
    for hand in player_deck:
        player_total += int(hand)

    #check if the dealer needs to pull another card
    if dealer_total <= 16:
        dealer_hand.append(deck_of_cards())
        dealer_total = 0
        for hand in dealer_hand:
            dealer_total += int(hand)
    
    #Print Hands and give win conditions
    print(f"Your hand is {', '.join(player_deck)} Your total points are {player_total}")
    print(f"The dealer's hand is {', '.join(dealer_hand)}  The Dealers total points are {dealer_total}")


    #check if dealer busted
    if dealer_total > 21:
        print("You Win! The dealer busted!")
    #check if the player beat the dealer
    elif player_total > dealer_total:
        print("You beat the Dealer and won the bet!") 
    #check if the dealer beat the player
    elif player_total < dealer_total:
        print("The dealer beat you. You lose!")
    else:
        print("You matched the Dealer. You get your bet back")

    replay = str(input("Would you like to play again? (Y or N) "))
    replay.lower()
    return replay


print("Welcome to the Black Jack Game")
start = ""
start = input("Would you like to start playing? (Y or N) ")
start = start.lower()

while start == "y":
    start = Black_Jack()
    start = start.lower()
    
