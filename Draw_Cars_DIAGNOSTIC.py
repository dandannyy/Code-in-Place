# DIAGNOSTIC 5
"""
Fix this program so that it does what it is meant to. You can make changes to both draw_car and main, but draw_car must implement the functionality described in its comment. 
Write a comments for each line you changed.
Note that you should assume that the offsets in draw_car are correct. You are not meant to be worrying about the canvas coordinates, rather the control flow of the program.
"""

from graphics import Canvas

def main():
    # draws two cars
    canvas = Canvas(400, 400) 
    x = 10 
    y = 10
    draw_car(canvas, x, y) # parameters for the first car

    x = 100
    y = 100
    draw_car(canvas, x, y) # parameters for the second car

def draw_car(canvas, x, y): #parameters
    # draws a car at the location x, y
    # you can assume that math offsets for the rectangles are correct
    canvas.create_rectangle(x, y, x + 50, y + 20)
    canvas.create_rectangle(x + 10, y - 10, x + 40, y + 20)

if __name__ == '__main__':
    main()
