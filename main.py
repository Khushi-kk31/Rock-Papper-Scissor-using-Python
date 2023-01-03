#************************************Rock Paper Scissor Game******************************

import random

def gameDecision(randNum,a):
    if randNum == 1:
        print("Computer --> Rock")
        if a == 1:
            print("Game is a Tie")
        elif a == 2:
            print("You win")
        elif a == 3:
            print("You lose")
    elif randNum ==2:
        print("Computer --> Paper")
        if a == 1:
            print("You lose")
        elif a == 2:
            print("Game is a Tie")
        elif a == 3:
            print("You win")
    else:
        print("Computer --> Scissor")
        if a == 1:
            print("You win")
        elif a == 2:
            print("You lose")
        elif a == 3:
            print("Game is a Tie")
    
    if a == 1:
        print("You --> Rock")
    elif a == 2:
        print("You --> Paper")
    elif a == 3:
        print("You --> Scissor")
    



print("*******************************Rock Paper Scissor Game******************************")
while True:
    print("Press 1 for Rock\t Press 2 for Paper\tPress 3 for Scissor\n  ")
    print("Computer's Turn-----\nComputer Turn is Over..\n")
    randNum = random.randint(1,3)
    print("Player's Turn-----")
    a = int(input('Press 1 for Rock\t Press 2 for Paper\tPress 3 for Scissor\n'))

    if a == 1 or a == 2 or a == 3:
        gameDecision(randNum, a)

    else:
        print("\nInvalid Input")

    print("\nPress 0 to exit:\nPress any number to continue")
    if input() == "0":
        exit()
