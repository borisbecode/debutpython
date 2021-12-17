from random import randint

possibility = ["rock","paper","scissors"]
player = None
while True:
    computer = possibility[randint(0,2)]
    player = input("rock , paper or scissors? (or stop the game?) ").lower()
    print("computer choice : ",computer)
    print("playerchoice : " , player)


    if player == "stop the game":
        print("the game is finish because you are virgin")
        break
    elif player == computer: 
        print("It's a draw !")


    elif player == 'rock':
        if computer == "paper":
            print ("you lose ")
        else:
            print("you win BOUGAHBOUGAH !")


    elif player == 'paper':
        if computer == "scissors":
            print ("you lose ")
        else:
            print("you win BOUGAHBOUGAH !")

    elif player == 'scissors':
        if computer == "rock":
            print ("you lose ")
        else:
            print("you win BOUGAHBOUGAH !")

    else:
        print(" bad entries ! ")
    

    play_again = input("play again? (yes/no)").lower()
    if play_again != "yes":
        break


print("go cry in your mother's arms")


