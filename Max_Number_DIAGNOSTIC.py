# DIAGNOSTIC 2
"""
Print out each of the numbers 1 through 100 and whether that number is even or odd.
100 is specified using a constant MAX_NUMBER.
"""

# print numbers from 1 up until MAX_NUMBER, inclusive
MAX_NUMBER = 100

def main():
    for i in range(1, MAX_NUMBER + 1): # + 1 to account for 100
        if i % 2 == 0:
            print(f"{i} is even")
        else:
            print(f"{i} is odd")

if __name__ == "__main__":
    main()
