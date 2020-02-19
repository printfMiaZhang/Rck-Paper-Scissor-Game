from random import randint


t = ["Rock", "Paper", "Scissor"]

computer = t[randint(0, 2)]

player = False

while player == False:

    player = input("Rock, Paper, Scissor?")

    if player == computer:
        print("Tie!")

    elif player == "Rock":
        if computer == "Paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes ", computer)
    elif player == "Scissor":
        if computer == "Rock":
            print("You lose!", computer, " smashes ", player)
        else:
            print("You win!", player, " cuts ", computer)
    elif player == "Paper":
        if computer == "Scissor":
            print("You lose!", computer, " cuts ", player)
        else:
            print("You win!", player, "covers", computer)
    else:
        print("Invalid entry. Check your spelling!")

    player = False
    computer = t[randint(0, 2)]
