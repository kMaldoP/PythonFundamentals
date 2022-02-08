import random

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []


while diamonds:
    card = input("Press Enter to pick a card or Q then Enter to quit:")
    if card == "":
        card = diamonds.pop(random.randrange(len(diamonds)))
        hand.append(card)
        print("Your hand: ", hand)
        print("Remaining cards: ", diamonds)
    elif card == "Q" or card == "q":
        print("Thanks for playing!")
        break
    else:
        print("Invalid option")

if not diamonds:
    print("There are no more cards to pick!")
