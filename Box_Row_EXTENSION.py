# Week 5
"""
Change CANVAS_HEIGHT to be 400 and see if you can fill the entire canvas with boxes to make a 5x5 grid of squares!
"""

from graphics import Canvas

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
N_BOXES = 5
BOX_SIZE = CANVAS_WIDTH / N_BOXES

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    for i in range(N_BOXES): # for loops to rows
        for f in range(N_BOXES): # for loops to columns
            left_x = i * BOX_SIZE # will repeat rows
            top_y = f * BOX_SIZE # will repeat columns
            right_x = left_x + BOX_SIZE # will add the boxes
            bottom_y = top_y + BOX_SIZE # will add the boxes
            canvas.create_rectangle(
                left_x, 
                top_y, 
                right_x, 
                bottom_y, 
                "white", 
                "black")

if __name__ == '__main__':
    main()
