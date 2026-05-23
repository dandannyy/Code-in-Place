# Week 5
"""
Let's practice making graphics with lots of repeated elements. 
This will help us get familiar with working with multiple shapes and pixel calculations!
Make a line of boxes as shown below, such that the boxes fill the bottom of the canvas. 
Each box should have a width and height of BOX_SIZE, making a total of 5 boxes perfectly in line with one another
"""

from graphics import Canvas

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 200
N_BOXES = 5
BOX_SIZE = CANVAS_WIDTH / N_BOXES

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    for i in range(N_BOXES):
        left_x = i * BOX_SIZE 
        top_y = CANVAS_HEIGHT - BOX_SIZE # will only occupy half
        right_x = left_x + BOX_SIZE # will add the boxes
        bottom_y = CANVAS_HEIGHT # start from bottom
        canvas.create_rectangle(
            left_x, 
            top_y, 
            right_x, 
            bottom_y, 
            "white", 
            "black")

if __name__ == '__main__':
    main()
    
