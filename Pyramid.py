# Week 5 (OPTIONAL)
"""
Write a program that draws a pyramid consisting of bricks arranged in horizontal rows, so that the number of bricks in each row decreases by one as you move up the pyramid. 
The pyramid should be centered at the bottom of the drawing canvas and should use constants.
"""

from graphics import Canvas
import random

CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 300     # Height of drawing canvas in pixels

BRICK_WIDTH	= 30        # The width of each brick in pixels
BRICK_HEIGHT = 12       # The height of each brick in pixels
BRICKS_IN_BASE = 14     # The number of bricks in the base

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    for row in range(BRICKS_IN_BASE): # create row by row
        bricks_in_row = BRICKS_IN_BASE - row # how many bricks will there be in that row (decresing one by one, until the top)
        total_row_width = bricks_in_row * BRICK_WIDTH 
        start_x = (CANVAS_WIDTH - total_row_width + BRICK_WIDTH * 2) / 2 # centered row
        y = CANVAS_HEIGHT - BRICK_HEIGHT * (row + 1) # draw from base to top, defined the height of the row
        for brick in range(bricks_in_row):
            x = start_x + brick * BRICK_WIDTH # calculate the position of the brick
            canvas.create_rectangle(
                x, # top left
                y, # top left
                x - BRICK_WIDTH, # bottom right
                y + BRICK_HEIGHT, # bottom right
                "yellow",
                "black")

if __name__ == '__main__':
    main()
