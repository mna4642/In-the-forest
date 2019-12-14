"""This is a demo of the Snowflakes"""

import turtle as turtle
import random
import sys
import colorsys

# global constants for window dimensions
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

def init():
    """Initialize for drawing. (-200,-400) is in the lower left and
    (800, 800) is in the upper right.
    :pre: pos (800, 400), heading (east), up
    :post: pos (0,0), heading (east), up
    :return: None
    """
    turtle.setworldcoordinates(-WINDOW_WIDTH, -WINDOW_WIDTH, WINDOW_WIDTH, WINDOW_HEIGHT)
    turtle.speed(0)
    turtle.hideturtle()

def drawFlake1(length, depth):
    "draws a flake"
    if depth > 0:
        for _ in range(6):
            turtle.forward(length)
            drawFlake1(length // 3, depth - 1)
            turtle.backward(length)
            turtle.left(60)

def drawFlake2(length, depth):
    "draws a flake"
    if depth > 0:
        for _ in range(6):
            turtle.forward(length)
            drawFlake2(length // 3, depth - 1)
            turtle.backward(length)
            turtle.left(60)

def drawFlake3(length, depth):
    "draws a flake"
    if depth > 0:
        for _ in range(6):
            turtle.forward(length)
            drawFlake3(length // 3, depth - 1)
            turtle.backward(length)
            turtle.left(60)

def drawFlake4(length, depth):
    "draws a flake"
    if depth > 0:
        for _ in range(6):
            turtle.forward(length)
            drawFlake4(length // 3, depth - 1)
            turtle.backward(length)
            turtle.left(60)



def main():
    """
    The main function.
    :pre: pos (0,0), heading (east), up
    :post: pos (0,0), heading (east), up
    :return: None
    """
    init()
    drawFlake1(200, 1)
    input("Picture one is done. Press enter for picture two.")
    turtle.clear()
    drawFlake1(200, 2)
    input("Picture two is done. Press enter for picture three.")
    turtle.clear()
    drawFlake3(200, 3)
    input("Picture three is done. Press enter for picture four.")
    turtle.clear()
    drawFlake4(200, 4)
    input("Picture four is done. Press enter to exit.")
    turtle.bye()

    turtle.mainloop()

if __name__ == "__main__":
        depth = 3
if len(sys.argv) >= 2:
        depth = int(sys.argv[1])

main()
