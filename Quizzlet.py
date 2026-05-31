# Week 6
"""
Write a program that loops over a dictionary of words and quizzes the user for their corresponding Spanish translations, keeping count of how many the user gets correct! 
Separate each question and answer with a blank line to help with visual clarity.
"""

def main():
    translations = {
        "hello": "hola",
        "dog": "perro",
        "cat": "gato",
        "well": "bien",
        "us": "nos",
        "nothing": "nada",
        "house": "casa",
        "time": "tiempo"
    }
    correct_count = 0
    for english, spanish in translations.items():
        print(f"What is the Spanish translation for {english}?")
        your_answer = input()
        if your_answer == spanish:
            print("That is correct!")
            correct_count = correct_count + 1
        else:
            print(f"That is incorrect, the Spanish translation for {english} is {spanish}.")
    print()
    print(f"You got {correct_count}/{len(translations)} words correct, come study again soon!")

if __name__ == '__main__':
    main()
