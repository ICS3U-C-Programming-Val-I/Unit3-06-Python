#!/usr/bin/env python3

# Created By: Val Ijaola
# Date: October 25, 2023
# This program chooses a random number then asks the user to
# guess it, then it checks if the entered an integer
# and lets them know if they are right.

import random


def main():
    # input - get guess from user.
    user_guess_as_string = input("Pick a number between 0 and 9\n")

    # process - set correct answer and check guess.
    correct_answer = random.randint(0, 9)
    try:
        user_guess_as_int = int(user_guess_as_string)
    except ValueError:
        print(f"{user_guess_as_string} is not an integer.")
    else:
        if correct_answer == user_guess_as_int:
            # output - display result
            print("Correct, you got it right.")
        else:
            # output - display result
            print(f"Incorrect, the correct number is {correct_answer}")
    finally:
        print("thanks for playing")


if __name__ == "__main__":
    main()
