# DIAGNOSTIC 1
"""
Write a console program which asks the user for their height in meters and prints whether or not they are the correct height to be a NASA astronaut.
-If their height is greater than 1.6 meters and less than 1.9 meters, print 
"Correct height to be an astronaut".
-If their height is less than or equal to 1.6 meters, print 
"Below minimum astronaut height".
-If their height is greater than or equal to 1.9 meters, print 
"Above maximum astronaut height".
"""

def main():
    user_height = float(input("Enter your height in meters: "))
    if user_height > 1.6 and user_height < 1.9:
        print("Correct height to be an astronaut")
    elif user_height <= 1.6:
        print("Below minimum astrounat height")
    else:
        print("Above maximum astronaut height")

if __name__ == "__main__":
    main()
