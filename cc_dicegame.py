import random

high_score = 0

choice_1_acc_terms = ["1", "yes, lets do this", "yes", "lets do this"]
choice_2_acc_terms = ["2", "no, i dont want to have any fun", "no"]

def dice_game():
    global high_score
    print(f"Current High Score: {high_score}")
    print("Welcome to the dice game, are you ready to play?")
    choice = input("1) Yes, Lets do this\n2) No, I dont want to have any fun")
    
    while True:
        if choice  in choice_1_acc_terms:
            dice1 = random.randint(1,6)
            dice2 = random.randint(1,6)
            combined_roll_total = dice1 + dice2
            print(f"You have rolled a {dice1} and a {dice2}\nYou have a total of {combined_roll_total}")
            continue
        if combined_roll_total > high_score:
            high_score = combined_roll_total
            print("A new high score!")
            break
        if combined_roll_total == 12:
            print("Double sixes, you win the game!")
        else:
           break

        if choice in choice_2_acc_terms:
            print("Goodbye! See you next time!")
        else:
            print("That was not a valid option, please enter a valid selection")
            break

dice_game()