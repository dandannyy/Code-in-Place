# Week 5 
""""
Students in Code in Place are from 150 different countries! Wow. Let's celebrate our international class by drawing flags. 
To start out, one of the most straightforward flags to draw using Python graphics is the flag of Indonesia
""""
from graphics import Canvas
import random

CANVAS_WIDTH = 450
CANVAS_HEIGHT = 300

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    left_x = 0 # both starts from top left of the rectangle
    top_y = 0
    right_x = CANVAS_WIDTH
    bottom_y = CANVAS_HEIGHT/2
    rect = canvas.create_rectangle(
        left_x, 
        top_y, 
        right_x,
        bottom_y,
        'red')
    
if __name__ == '__main__':
    main()
