# Week 4
"""
Write a program that prints out the calls for a spaceship that is about to launch. 
Countdown from 10 to 1 and then output Liftoff!
"""

def main():
    for i in range(10, 0, -1): #10 it's the start, 0 it's the final and -1 it's invert the order(crescent)
        print(i)
    print("Liftoff!")

if __name__ == '__main__':
    main()
