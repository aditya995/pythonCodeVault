# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to
# guess the number, then tell them whether they guessed too low, too high, or 
# exactly right.

# Extras:
# 1.Keep the game going until the user types “exit”
# 2.Keep track of how many guesses the user has taken, and when the game ends, 
# print this out.

import random as rd

while True:
    number = rd.randint(1,9)
    print("I have a number in my mind that is from 1 to 9. Please guess a number.\nEnter 'exit' to exit anytime!")

    guess = None
    guess_number = 0
    while True:
        guess = input("Your guess in integer: ").lower()
        try:
            guess = int(guess)
            guess_number += 1
            if guess > number:
                print("Your guess is too high! Guess again.")
            if guess < number:
                print("Your guess is too low! Guess again.")
            if guess == number:
                print(f"Wowee! You've guessed my number ({guess})! You took {guess_number} tries.")
                break
        except Exception:
            if guess == 'exit':
                break
            else:
                print('Give integer input, or enter "exit" to end the game')
    if guess == 'exit' or input("Do you want to play again? (Y/N): ") == "N":
        break