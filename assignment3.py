import random

correct_g = 0
incorrect_g = 0

print("This is the game of heads or tails")

while True:

    guess = input("Enter 'heads' or 'tails': ").lower()

    coin_flip = random.choice(["heads", "tails"])

    print(f"The coin landed on {coin_flip}!")

    if guess == coin_flip:
        print("You are correct!")
        correct_g +=1

    elif guess in ["heads", "tails"]:
        print("Incorrect!")
        incorrect_g +=1
    
    else:
        print("invalid input")

    again = input("Would you like to play again?").lower()

    if again == "no":
        print(f"Okay, you had {correct_g} correct guesses and {incorrect_g} incorrect guesses")
        break