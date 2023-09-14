## Generate a random number
import random
answer = random.randint(1, 10)

## While loop keeps the user guessing and gives them feedback until they guess correctly
while True:
    try:
        guess = int(input(f"Enter a number between 1 and 10: "))
        if 1 <= guess <= 10:
            if guess < answer:
                print(f"Your guess {guess} was too low. Please try again.")
            elif guess > answer:
                print(f"Your guess {guess} was too high. Please try again.")
            else:
                print(f"Congratulations, your guess {guess} is right!")
                break
        else:
            print(f"Please enter a number between 1 and 10.")
    except ValueError:
        print(f"Invalid input. Please enter a valid number.")