from karel.stanfordkarel import *

# Week 1
"""
Karel should finish the puzzle by picking up the last beeper 
(puzzle piece) and placing it in the right spot. Karel should 
end in the same position Karel starts in -- the bottom left 
corner of the world.
"""

def main():
    go_puzzle()
    put_puzzle()
    back_position()

def go_puzzle():
    move_twice()
    pick_beeper()
    move()
    turn_left()

def put_puzzle():
    move_twice()
    put_beeper()

def back_position():
    turn_around()
    move_twice()
    turn_right()
    move_thrice()
    turn_around()
        
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def move_twice():
    move()
    move()

def turn_around():
    turn_left()
    turn_left()

def move_thrice():
    move()
    move()
    move()
    
if __name__ == '__main__':
    main()
