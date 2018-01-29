# Mark Sherriff (mss2x)

import random

print("Welcome to Pig!")
winning_score = int(input("What score would you like to play to?: "))
turn = input("Would you like to go first (y/n)?: ")
pig_number = int(input("What number would you like to result in a PIG?: "))

if (turn == 'y'):
    turn = "player"
else:
    turn = "computer"

done = False
player_temp_total = 0
player_total = 0
comp_temp_total = 0
comp_total = 0

while not done:
    while turn == "player" and not done:
        print()
        print("Player:", player_total, "Computer:", comp_total)
        print("It's your turn!")
        roll = random.randint(1,6)
        if roll == pig_number:
            turn = "computer"
            player_temp_total = 0
            print("You rolled a " + str(pig_number) + "! PIG! Too bad! Your total is currently:", player_total)
        else:
            player_temp_total += roll
            print("You rolled a", roll, "and now have " + str(player_temp_total) + " banked.")
            choice = input("Do you wish to roll again (y/n)?: ")
            if choice == 'n':
                player_total += player_temp_total
                player_temp_total = 0
                print("Your total score is now:", player_total)
                turn = "computer"
        if player_total > winning_score:
            print("You win! " + str(player_total) + " to " + str(comp_total))
            done = True

    while turn == "computer" and not done:
        print()
        print("Player:", player_total, "Computer:", comp_total)
        print("It's the computer's turn!")
        roll = random.randint(1,6)
        if roll == pig_number:
            turn = "player"
            comp_temp_total = 0
            print("The computer rolled a " + str(pig_number) + "! PIG! Too bad! The computer's total is currently:", comp_total)
        else:
            comp_temp_total += roll
            print("The computer rolled a", roll, "and now has " + str(comp_temp_total) + " banked.")
            if comp_temp_total > 6 or comp_total + comp_temp_total > winning_score:
                print("The computer has chosen to end its turn.")
                comp_total += comp_temp_total
                comp_temp_total = 0
                print("The computer's score is now:", comp_total)
                turn = "player"
        if comp_total > winning_score:
            print("The computer wins! " + str(comp_total) + " to " + str(player_total))
            done = True