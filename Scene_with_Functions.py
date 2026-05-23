# Week 5
"""
In this assignment, you will draw a natural scene while practicing how to break a program into functions with parameters. 
You are also being given an AI code-completion tool for this assignment. The tool can suggest code, but you are responsible for reading the generated code 
carefully and deciding whether it is correct.
This assignment is self-graded. When you have visited the page, read this disclosure, and tried the assignment, use the normal mark-complete action to 
acknowledge participation and complete it.
"""

from graphics import Canvas
import math
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 300

CLOUD_WIDTH = 120
CLOUD_HEIGHT = 80

TRUNK_HEIGHT = 80
TRUNK_WIDTH = 20
LEAVES_SIZE = 60

TREE_BOTTOM_Y = CANVAS_HEIGHT - 20 

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    draw_cloud(canvas, 140, 10, 'salmon')
    draw_cloud(canvas, 20, 50, 'pink')
    draw_cloud(canvas, 260, 35, 'purple')
    draw_tree(canvas, 40, 220, 'green')
    draw_tree(canvas, 120, 220, 'red')
    draw_tree(canvas, 300, 220, 'orange')

def draw_cloud(canvas, x, y, color):
    """
    This function draws one cloud. You can call it and pass in 
    different values of x and y (the location of the cloud) and
    color (the color of the cloud). 
    """
    cloud_bottom_start_y = y + (1/3) * CLOUD_HEIGHT
    cloud_bottom_end_y = y + CLOUD_HEIGHT
    cloud_top_start_x = x + (1/4) * CLOUD_WIDTH
    cloud_top_end_x = x + (3/4) * CLOUD_WIDTH
    # Bottom two puffs
    canvas.create_oval(
        x, 
        cloud_bottom_start_y,
        x + (3/4) * CLOUD_WIDTH,
        cloud_bottom_end_y,
        color)
    canvas.create_oval(
        x + (1/4) * CLOUD_WIDTH, 
        cloud_bottom_start_y,
        x + CLOUD_WIDTH,
        cloud_bottom_end_y,
        color)

    # Top puff
    canvas.create_oval(
        cloud_top_start_x,
        y,
        cloud_top_end_x,
        y + (2/3) * CLOUD_HEIGHT,
        color)

def draw_tree(canvas, x, y, color):
    canvas.create_rectangle(
        x,
        y - 10,
        x + TRUNK_WIDTH,
        y + (2/3) * TRUNK_HEIGHT,
        'brown')
    canvas.create_oval(
        x - 20,
        y - LEAVES_SIZE,
        x + 40,
        y,
        color)

if __name__ == '__main__':
    main()
