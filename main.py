import random
import sys

options = ("rock", "paper", "scissors")

wins = 0
losses = 0
ties = 0
while True:
    computer = random.choice(options)
    player = input("Choose between Rock, Paper, Scissors: (q to quit)").strip().lower()

    i = 0
    while player not in options and player != "q":
        if i == 4:
            print("You have been blocked!")
            sys.exit()
        print("Please enter a valid choice")
        print(f"{4 - i} attempts remaining! ")
        player = input("Choose between Rock, Paper, Scissors: ").strip().lower()
        i += 1
    if player != "q":
        print(f"Player: {player}")
        print(f"Computer: {computer}")
        if player == computer:
            print("It's a tie!")
            ties += 1
        elif player == "Rock" and computer == "Scissors":
            print("You win!")
            wins += 1
        elif player == "Scissors" and computer == "Paper":
            print("You win!")
            wins += 1
        elif player == "Paper" and computer == "Rock":
            print("You win!")
            wins += 1
        else:
            print("You lose! ")
            losses += 1

    if player == "q":
        print("It was nice playing with you!")
        print("-----Results-----")
        print(f"Wins: {wins}")
        print(f"Losses: {losses}")
        print(f"Ties: {ties}")
        break
    else:
        print("-----Results-----")
        print(f"Wins: {wins}")
        print(f"Losses: {losses}")
        print(f"Ties: {ties}")
        print("-----New Round-----")
