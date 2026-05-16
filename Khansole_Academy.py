import random

# Week 4
"""
Write a program that randomly generates a simple addition problem for the user, reads in the answer from the user, and then checks to see if they got it right or wrong.
More specifically, your program should be able to generate simple addition problems that involve adding two 2-digit integers (i.e., the numbers 10 through 99). 
The user should be asked for an answer to the generated problem. 
Your program should determine if the answer was correct or not, and give the user an appropriate message to let them know.
"""

def main():
    print("Khansole Academy")
    secret_addition1 = random.randint(10, 99)
    secret_addition2 = random.randint(10, 99)
    addition = secret_addition1 + secret_addition2
    print(f"What is {secret_addition1} + {secret_addition2}?")
    your_answer = int(input("Your answer: "))
    if your_answer == addition:
        print("Correct!")
    else:
        print("Incorrect.")
        print(f"The expected answer is {addition}")
    
if __name__ == '__main__':
    main()
