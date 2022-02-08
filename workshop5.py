import random


def guess_random_number(tries, start, stop):
    piv = random.randint(start, stop +1)
    print(f"Number is {piv}")

    if tries == 0:
        print("You have run out of guesses #WOMP WOMP ")
    while tries != 0:
        print(f"Number of tries remaining: {tries}")
        user_guess = int(input("guess a number between 0 and 10  "))
        if user_guess == piv:
            print("You nailed it!")
            return
        elif user_guess < piv:
            print("Guess higher! ") 
        elif user_guess > piv:
            print("Guess lower! ")


        tries -= 1
    if tries == 0:
        print(f"You have run out of guesses #WOMP WOMP \nThe number was {piv} ")

#guess_random_number(2, 0, 100)


def guess_random_num_linear(tries, start, stop):
    piv = random.randint(start, stop + 1)    
    print(f"Number is {piv}")

    for x in range(start, stop +1):
        print(f"program is guessing...  {x}")
        if x == piv:
            print(f"The program has guessed the correct number!")
            return
        if tries == 0:
            print("The program has failed to guess the correct number")
            return
        tries -= 1

#guess_random_num_linear(3, 1, 20)


def binary_search(the_list, target, tries):
    lower_bound = 0
    upper_bound = len(the_list) - 1
    while lower_bound <= upper_bound:
        if tries == 0:
            print(f"You lost! The correct answer is {target}")
        pivot = (lower_bound + upper_bound) // 2
        pivot_value = the_list[pivot]
        if pivot_value == target:
            print("good job")
            return 
        if pivot_value > target:
            print(pivot_value)
            print("too high")
            upper_bound = pivot - 1
        else:
            print(pivot_value)
            print("too low")
            lower_bound = pivot + 1
            tries -= 1
    return -1

def guess_random_number_binary(tries, start, stop):
    piv = random.randint(start, (stop +1))
    the_list = list(range(start, stop +1))
    binary_search(the_list, piv, tries)
    print(the_list)
    
    
   

guess_random_number_binary(3, 1, 20)

