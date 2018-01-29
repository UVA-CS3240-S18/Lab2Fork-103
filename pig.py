# Mark Sherriff (mss2x)

import random
print()
print("Welcome to Pig!")
print("==================")
print("When it is your turn you may choose to roll or not roll a number from 1-6.")
print("Rolling a number from 2 to 5 adds it to your banked total")
print("Rolling a 1, resets your banked total, ends your turn, and starts the computer's turn.")
print("Choosing not to roll adds your banked total to your actual score, and switches turns")
print("==================")
done = False
player_temp_total = 0
player_total = 0
comp_temp_total = 0
comp_total = 0
turn = "player"
winning_score = 50

while not done:
    while turn == "player" and not done:
        print()
        print("Player:", player_total, "Computer:", comp_total)
        print("It's your turn!")
        roll = random.randint(1,6)
        print("You rolled a", roll)
        if roll == 1:
            turn = "computer"
            player_temp_total = 0
            print("PIG! Too bad! Your total is currently:", player_total)
        else:
            player_temp_total += roll
            print("You currently have " + str(player_temp_total) + " banked.")
            choice = input("Do you wish to roll again (y/n)?: ")
            if choice == 'n':
                player_total += player_temp_total
                player_temp_total = 0
                print("Your total socre is now:", player_total)
                turn = "computer"
        if player_total > winning_score:
            print("You win! " + str(player_total) + " to " + str(comp_total))
            done = True

    while turn == "computer" and not done:
        print()
        print("Player:", player_total, "Computer:", comp_total)
        print("It's the computer's turn!")
        roll = random.randint(1,6)
        print("The computer rolled a", roll)
        if roll == 1:
            turn = "player"
            comp_temp_total = 0
            print("PIG! Too bad! The computer's total is currently:", comp_total)
        else:
            comp_temp_total += roll
            print("The computer has " + str(comp_temp_total) + " banked.")
            if comp_temp_total > 6 or comp_total + comp_temp_total > winning_score:
                print("The computer has chosen to end its turn.")
                comp_total += comp_temp_total
                comp_temp_total = 0
                print("The computer's score is now:", comp_total)
                turn = "player"
        if comp_total > winning_score:
            print("The computer wins! " + str(comp_total) + " to " + str(player_total))
            done = True