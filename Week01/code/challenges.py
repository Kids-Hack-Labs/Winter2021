"""
    Kids Hack Labs
    Winter 2021 Term
    Week 01
    Homework Challenges: Number-guessing game

    Note: Both challenges implemented at the same time
          No extensions are marked as such, only challenges
          The score system works by adding remaining tries as points,
          meaning it's possible to get 0 points despite winning
"""

import random

def main():
    random.seed()
    player = input("Hello, what is your name? ")
    print(f"Welcome to KHL\'s number-guessing game, {player}")

    #Challenge 10: Multi-round variables
    score = 0
    wins = 0
    total_rounds = 0
    round_won = False
    playing = True

    #Challenge 10: Multi-round implementation
    while playing:
        lowest = int(input("What is the lowest number in the range? "))
        highest = int(input("What is the highest number in the range? "))

        #Challenge 11: Data validation
        while highest <= lowest:
            print(f"Highest number cannot be equal to or lower than {lowest}.")
            highest = int(input("What is the highest number in the range?"))

        print(f"Setting mystery number between {lowest} and {highest}...")
        target = random.randrange(lowest, highest)
        print("Mystery number set!")

        max_tries = int(input("How many tries do you want to get?"))

        #Challenge 11: Data validation
        while max_tries >= (highest - lowest):
            print("Not allowed. Max guesses must be less than range of numbers")
            max_tries = int(input("How many tries do you want to get?"))

        tries = max_tries
        round_won = False
        in_round = True
        total_rounds += 1

        while in_round:
            answer = input(f"Guess a number between {lowest} and {highest},\n"+
                           "\"q\" or \"Q\" to quit: ")
            
            if answer.lower() == "q":
                in_round = False
                playing = False
                break
            else:
                answer = int(answer)

                #Challenge 11: data validation
                if not lowest <= answer <= highest:
                    print("Guess outside range. Try again.")
                    continue

            tries -= 1
            if answer == target:
                round_won = True
                in_round = False
            elif answer < target:
                print(f"Too low. You have {tries} tries left.")
            else:
                print(f"Too high. You have {tries} tries left.")

            if tries == 0:
                in_round = False

        if playing:
            if round_won:
                print(f"Congrats, {player}!"+
                      f"You won this round after {max_tries - tries} tries")
                wins += 1
                score += tries
            else:
                print(f"Sorry, {player}. You lost this round."+
                      f"The mystery number was {target}")
                
            #Challenge 10: Replay round mechanic
            replay = input("Do you want to play again? (Y/y, N/n) ").lower()

            #Challenge 11:Data validation
            while replay != "y" and replay != "n":
                replay = input("Do you want to play again? (Y/y, N/n) ").\
                             lower()

            #Note: this boolean expression evaluates to True if the
            #      user chooses "yes", or to false if the user chooses "no"
            playing = (replay != "n")

    print(f"Here is a breakdown of your performance, {player}:\n"+
          f"Rounds Played: {total_rounds}\n"+
          f"Rounds Won: {wins}\n"+
          f"Final Score: {score}")

if __name__ == "__main__":
    main()
