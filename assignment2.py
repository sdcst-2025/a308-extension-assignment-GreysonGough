from random import randint

rnum = randint(1, 100)

guess_count = 0
 
print("The number is from 1 - 100")

while True:
    try:
        guess_count += 1
        guess = int(input(f"Enter your guess: "))

        if guess < 1 or guess > 100:
            print("Please guess within 1 - 100.")

        elif guess == rnum:
            print(f"congrats you won. {guess_count} guesses.")
            break

        elif guess < rnum:
            print("Too low! Please try again")

        elif guess > rnum:
            print("Too high! Please try again")

    except ValueError:
        print("Please enter a valid value.")
        guess_count += 1



