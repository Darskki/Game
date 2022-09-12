import random
from RPS_package import rock, paper, scissors

game_images = [rock, paper, scissors]

user_choice = int(input("What do you want to choose? Type>  (0) Rock / (1) Paper/ (2) Scissors.\n"))

if user_choice >= 3 or user_choice < 0:
    print("\nYou typed an invalid number, you lose!")
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print(f"Computer chose:")
    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("\nYou win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose.")
    elif computer_choice > user_choice:
        print("You lose!")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It is a draw.")
