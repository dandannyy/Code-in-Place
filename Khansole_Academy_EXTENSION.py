import random

# Week 4
"""
Three in a row
In the previous milestone you wrote code to randomly generate one addition problem at a time and tell the user if they got it right or not. 
In this milestone, you should randomly generate addition problems until the user has gotten 3 problems correct in a row. 
(Note: the number of problems the user needs to get correctly in a row to complete the program is just one example of a good place to specify a constant in your program).
"""

def main():
    print("Khansole Academy")
    count_your_answer = 0 # The variable for the extension
    while count_your_answer < 3: # Continue generating additions until you get 3 correct answers in a row
        secret_addition1 = random.randint(10, 99)
        secret_addition2 = random.randint(10, 99)
        addition = secret_addition1 + secret_addition2
        print(f"What is {secret_addition1} + {secret_addition2}?")
        your_answer = int(input("Your answer: "))
        if your_answer == addition:
            print("Correct!")
            count_your_answer = count_your_answer + 1 # Counting the correct one
            print(f"You've gotten {count_your_answer} in a row.")
        else:
            print("Incorrect.")
            print(f"The expected answer is {addition}")
    print("Congratulations! You mastered addition.") # If you get 3 correct answers in a row, no more additions will be genereated and a mensage will appear
    
if __name__ == "__main__":
    main()
