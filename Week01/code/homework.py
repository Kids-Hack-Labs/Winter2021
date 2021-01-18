"""
    Kids Hack Labs
    Winter 2021 term
    Week 01
    Homework: Number-guessing game extensions

    Note 1: f-strings are compatible with Python 3.6 or higher.
            Older versions of Python require string concatenation
            and may also require type conversion for proper output
    Note 2: Extension 01 is commented out.
"""

import random

def main():
    random.seed()
    #Extension 01:
    #random.seed(4) #target will always be 31 in the range 1-100
    
    #Extension 02:
    print("Welcome to KHL's number-guessing game")

    #Extension 09:
    player = input("What is your name? ")
    
    #Extension 03:
    bottom = int(input("What is the lowest number in the range? "))
    top = int(input("What is the highest number in the range? "))
    target = random.randrange(bottom, top)
    
    #Extension 04 (includes Extension 09 and setup for Extensions 06 and 07):
    max_tries = int(input(f"How many chances do you want, {player}? "))
    tries = max_tries
    
    playing = True
    won = False

    while playing:
        guess = int(input(f"Guess a number between {bottom} and {top}: "))
        tries -= 1

        if guess == target:
            won = True
            playing = False
        else:
            #print("Wrong guess...") #original
            #Extension 05
            if guess < target:
                print("You guessed lower than the target number.")
            else:
                print("You guessed higher than the target number.")
            #Extension 06
            print(f"You have {tries} tries left, {player}.")

        if tries == 0:
            playing = False

    if won:
        #print("Congratulations! You guessed the mystery number.") #original
        #Extension 07:
        print(f"Congratulations, {player}! "+
              "You guessed the mystery number "+
              f"in {max_tries - tries} tries.")
    else:
        #print("You ran out of tries...") #original
        #Extension 08:
        print(f"You ran out of tries, {player}."+
              f"The mystery number was {target}")

if __name__ == "__main__":
    main()
