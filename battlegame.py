wizard = "wizard"
wizard_hp = 70
wizard_damage = 150
elf = "elf"
elf_hp = 100
elf_damage = 100
human = "human"
human_hp = 150
human_damage = 20
dragon_hp = 300
dragon_damage = 50
orc = "orc"
orc_hp = 125
orc_damage = 115
mom = "mom"
mom_hp = 125
mom_damage = 75

while True:
    print(" 1) wizard \n 2) elf \n 3) human \n 4) orc \n 5) Mom")
    character = input("Choose your character: ".lower())
    if character == "1" or character == "wizard":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
        break
    elif character == "2" or character == "elf":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
        break
    elif character == "3" or character == "human":
        character = human
        my_hp = human_hp
        my_damage = human_damage
        break
    elif character == "4" or character == "orc":
        character = orc
        my_hp = orc_hp
        my_damage = orc_damage
        break
    elif character == "5" or character == "mom":
        character = mom
        my_hp = mom_hp
        my_damage = mom_damage
        break
    print("Unkown Character")
print(f" You have chosen the character: {character} \n HP: {my_hp}\n Damage: {my_damage} ")

while True:
    dragon_hp -= my_damage
    print(f"Your {character} damaged the dragon! \n The dragons health is {dragon_hp} ")
    if dragon_hp <= 0:
        print("The Dragon has lost the battle!")
        break
    my_hp -= dragon_damage
    print(f"The dragon has damaged your {character} \n your {character}'s hitpoints are {my_hp} ")
    if my_hp <= 0:
        print(f"Your {character} has lost the battle!")
        break
