import random

# Week 4
"""
Print 10 random numbers in the range 1 to 100.
"""

N_NUMBERS = 10
MIN_VALUE = 1
MAX_VALUE = 100

def main():
    for i in range(N_NUMBERS): # Show just 10 numbers
        value = random.randint(MIN_VALUE,MAX_VALUE)
        print(value)

if __name__ == '__main__':
    main()
