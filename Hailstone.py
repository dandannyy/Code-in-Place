# Week 4(OPTIONAL)
"""
Write a program that implements the following process.
Have the user input a positive integer, call it n.
If n is even, divide it by two.
If n is odd, multiply it by three and add one.
Continue this process until n is equal to one.
"""

def main():
    my_num = int(input("Enter a number: "))
    while my_num != 1:
        remaider = my_num % 2
        if remaider == 1:
            new_number = 3 * my_num + 1
            print(f"{my_num} is odd, so I make 3n + 1: {new_number}")
            my_num = new_number
        else:
            three_float = my_num/2 # Casting your values back to an integer
            three_int = int(three_float)
            print(f"{my_num} is even, so I take half: {three_int}")
            my_num = three_int 

if __name__ == "__main__":
    main()
