# Week 6
"""
Write a program that has a user play a memory game using lists.
"""

import random

NUM_PAIRS = 3

def main():
    truth = []
    for i in range(NUM_PAIRS): # Milestone 1
        truth.append(i)
        truth.append(i)

    random.shuffle(truth) # Milestone 2

    displayed = ['*'] * len(truth) # Milestone 3

    while "*" in displayed: # Milestone 6
        print_board(displayed)
        first = get_valid_index(displayed, -1)
        second = get_valid_index(displayed, first)

        if truth[first] == truth[second]:
            displayed[first] = truth[first]
            displayed[second] = truth[second]

            print("Match!")
            clear_terminal()
        else:
            print("Value at index", first, "is", truth[first])
            print("Value at index", second, "is", truth[second])
            print("No match. Try again.")
            input("Press Enter to continue...")
            clear_terminal
    print_board(displayed)
    print("Congratulations! You won!")
    
def clear_terminal():
    for i in range(20):
      print('\n')

def print_board(displayed):
    print(displayed)

def get_valid_index(displayed, first): # Milestone 5
    while True:
        guess = input("Enter an index: ")
        while guess != "0" and guess != "1" and guess != "2" and guess != "3" and guess != "4" and guess != "5":
            print("Not a number. Try again.")
            guess = input("Enter an index: ")
        guess = int(guess)
    
        if guess < 0 or guess >= len(displayed):
            print("Invalid index. Try again.")
        elif displayed[guess] != "*":
            print("This number has already been matched. Try again.")
        elif guess == first:
            print("You entered the same index twice. Try again.")
        else:
            return guess

if __name__ == '__main__':
    main()
