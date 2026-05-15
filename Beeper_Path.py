from karel.stanfordkarel import *

# Week 1
"""
Write a program that makes Karel follow and travel past the end of a straight line of beepers so they can make it home! 
"""

def main():
    while beepers_present():
        move()

if __name__ == '__main__':
    main()
