import random

print("Monster at Random Place")

# It's basically random Dice Generator
# User will play a game like Monopoly
# but everytime player move 
# there will be a monster to defeat 

# List for Monster 
list_of_monster = ['Goblin', 'Orc', 'Boar', 'Snake', 'Bat', 'Hobgoblin', 'Wyvern', 'Dragon', 'Earth Dragon']

# Item for player
monster_drop_item = ['Sword', 'Spear', 'Bow', 'Shield', 'Dagger', 'Staff', '100G']

# Number of turn for user 
turn = 0

# System will ask user to know 
# how many box inside the board game
ask_how_many_block = int(input("How large map that you want: "))

# Number of Box inside the board game
number_of_block = ask_how_many_block

# System will ask user to throw dice 
ask_to_throw_dice = input("Throw a Dice: ")

if ask_to_throw_dice == "y":
    while turn < number_of_block:
        dice = random.randint(1,6)
        print("Player move", dice, "block")

        monster_dice = random.randint(1,6)

        # if function for player to meet some monsters
        if dice == monster_dice:
            monster = random.choice(list_of_monster)
            print("Player meet with", monster)
            turn += 1
            
            # Player will fight a monster and get a drop item
            while dice == monster_dice:
                print("Player slayed ", monster)
                
                # Player will get random drop item from monster
                drop_item = random.choice(monster_drop_item)
                print("You Got ", drop_item)
                break
        else:
            turn += 1
            continue


    if turn == number_of_block:
        print("Congratulations, You Win!!!")
