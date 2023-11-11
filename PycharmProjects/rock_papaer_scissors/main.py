import random


class colors:
    yellow = '\033[93m'
    reset = '\033[0m'
    red = '\033[31m'
    green = '\033[32m'


def winner(userChoice: int, compAnswer: int) -> [str, str]:
    if compAnswer == userChoice:
        return [colors.yellow, "Tie!"]
    elif compAnswer == 0:
        if userChoice == 1:
            return [colors.green, "Congratulations, you win!"]
        elif userChoice == 2:
            return [colors.red, "You lose:("]
    elif compAnswer == 1:
        if userChoice == 2:
            return [colors.green, "Congratulations, you win!"]
        elif userChoice == 0:
            return [colors.red, "You lose:("]
    elif compAnswer == 2:
        if userChoice == 0:
            return [colors.green, "Congratulations, you win!"]
        elif userChoice == 1:
            return [colors.red, "You lose:("]


print("Welcome to the game called \"Rock, Paper and Scissors\"")
while True:
    choice = input("""Please choose what to pick!(write your answer as integer):\n\t\t1)Rock\n\t\t2)Paper\n\t\t3)Scissors
-->>:""")
    if not choice.isdigit():
        print("Write an integer from 1 to 3")
        continue
    choice = int(choice) - 1
    if 0 > choice or choice > 2:
        print("Write an integer from 1 to 3")
        continue
    compChoice = random.randint(0, 2)
    game = ["rock", "paper", "scissors"]
    print(f"You chose {game[choice]}, computer chose {game[compChoice]}")
    a = winner(choice, compChoice)
    print(a[0], a[1], colors.reset, sep="")
    answer = input("Wanna play again?(y - yes, n - no): ")

    while answer != "y" and answer != "n":
        answer = input("y - yes, n - no: ")
    if answer == "y":
        continue
    else:
        print("Exiting...")
        break
