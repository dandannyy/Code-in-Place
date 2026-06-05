# DIAGNOSTIC 3
"""
Write a program that has Karel draw four small “waves.” Each wave is a triangle made up of three beepers. There should be a gap between each wave.
Karel starts in the bottom-left corner of the world, facing East. 
When the program ends, Karel should be in the bottom-right corner of the world. It does not matter which direction Karel is facing.
"""

from karel.stanfordkarel import *

def main():
    for i in range(4):
        wave_base()
        wave_column()
        return_base()
        if front_is_clear(): # to avoid front is blocked
            wave_steps()

def wave_base():
    put_beeper()
    move()
    put_beeper()

def wave_column():
    turn_left()
    move()
    put_beeper()

def return_base():
    turn_around()
    move()
    turn_left()

def wave_steps():
    move()
    move()

def turn_around():
    turn_left()
    turn_left()

if __name__ == '__main__':
    main()
