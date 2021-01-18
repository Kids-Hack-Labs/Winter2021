"""
    Kids Hack Labs
    Winter 2021 term
    Week 01
    Activity: Number-guessing game
"""

import random

def main():
    random.seed()
    target = random.randrange(1, 100)
    tries = 5
    playing = True
    won = False

    while playing:
        guess = int(input("Guess a number between 1 and 100: "))
        tries -= 1

        if guess == target:
            won = True
            playing = False
        else:
            print("Wrong guess...")

        if tries == 0:
            playing = False

    if won:
        print("Congratulations! You guessed the mystery number")
    else:
        print("You ran out of tries...")

if __name__ == "__main__":
    main()
