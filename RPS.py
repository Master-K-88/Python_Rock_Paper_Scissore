import random

exit = False
user_point = 0
computer_point = 0
options = ["R", "P", "S"]

while not(exit):
    user_input = input("Enter R for Rock, P for Paper, S for Scissors and E for Exit: ")
    computer_input = random.choice(options)

    if user_input == "E":
        print("Game ended")
        print(f'Your total score is {user_point} and computer point is {computer_point}')
        exit = True
        break

    if user_input == "R":
        if computer_input == "R":
            print("You input is rock")  
            print("Computer input is rock")
            print("It is a tie")
        elif computer_input == "P":
            print("You input is rock")
            print("Computer input is paper")
            print("Computer wins")
            computer_point += 1
        elif computer_input == "S":
            print("You input is rock")
            print("Computer input is Scissors")
            print("You wins")
            user_point += 1

    elif user_input == "P":
        if computer_input == "P":
            print("You input is paper")
            print("Computer input is paper")
            print("It is a tie")
        elif computer_input == "R":
            print("You input is paper")
            print("Computer input is rock")
            print("You wins")
            user_point += 1
        elif computer_input == "S":
            print("You input is paper")
            print("Computer input is Scissors")
            print("Computer wins")
            computer_point += 1

    elif user_input == "S":
        if computer_input == "S":
            print("You input is Scissors")
            print("Computer input is Scissors")
            print("It is a tie")
        elif computer_input == "R":
            print("You input is Scissors")
            print("Computer input is rock")
            print("Computer wins")
            computer_point += 1
        elif computer_input == "P":
            print("You input is Scissors")
            print("Computer input is Paper")
            print("You wins")
            user_point += 1

    elif user_input != "R" or user_input != "P" or user_input != "S":
        print("Invalid input")
        
