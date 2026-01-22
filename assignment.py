#! python3

# SD Computing Studies Assignment
import random

print("Lets play, Rock, Paper, Scissors, Lizard, Spock!")
print("Please choose one of the following.")

choices = ["Rock", "Paper", "Scissors", "Spock", "Lizard"] 

while True:
    player_choice = input("Rock, Paper, Scissors, Lizard, Spock (Case Sensitive):")


    while player_choice not in choices:
        print("Invalid choice")
        player_choice = input("Please enter Rock, Paper, Scissors, Lizard or Spock (Case Sensitive): ")

    computer_choice = random.choice(choices)

    if computer_choice == player_choice:
        print("it's a tie")

    elif player_choice == "rock" and computer_choice == "scissors" or \
        player_choice == "paper" and computer_choice == "rock" or \
        player_choice == "scissors" and computer_choice == "paper" or \
        player_choice == "spock" and computer_choice == "rock" or \
        player_choice == "paper" and computer_choice == "spock" or \
        player_choice == "rock" and computer_choice == "lizard" or \
        player_choice == "lizard" and computer_choice == "spock" or \
        player_choice == "spock" and computer_choice == "scissors" or \
        player_choice == "scissors" and computer_choice == "lizard" or \
        player_choice == "lizard" and computer_choice == "paper":

        print("You beat the computer, congrats.")
        break
    else:
        print("Computer wins.")
        break