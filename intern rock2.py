import random

choices = ["rock","paper","scissor"]

player1 = input("Choose rock,paper,or scissor: ")
computer_Choice = random.choice(choices)

print(f"You Choose {player1},and the computer chose: {computer_Choice}.")

if player1 == computer_Choice:
    print("It's a tie.....!")
elif (player1 == "rock" and computer_Choice == "scissors") or \
     (player1 == "paper" and computer_Choice == "rock") or \
     (player1 == "scissor" and computer_Choice == "paper"):
    print("You Win!.................")
else:
    print("Computer Wins!.........")
     
