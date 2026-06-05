# DIAGNOSTIC 4
"""
Write a program that asks the user to enter a sequence of "non-decreasing" numbers one at a time. Numbers are non-decreasing if each number is greater than or equal to the last.
When the user enters a number which is smaller than their previously entered value, the program is over. Tell the user how long their sequence was.
"""

def main():
    print("Enter a sequence of non-decreasing numbers.")
    count = 1 # starts with 1
    previous_num = float(input("Enter num: ")) 
    current_num = float(input("Enter num: "))
    while current_num >= previous_num:
        count = count + 1
        previous_num = current_num # updates the comparison reference 
        current_num = float(input("Enter num: ")) # next number
    print("Thanks for playing!")
    print("Sequence length:", count)

if __name__ == "__main__":
    main()
