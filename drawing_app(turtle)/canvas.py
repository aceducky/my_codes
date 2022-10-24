import random
import turtle
from turtle import *

Screen()
t = turtle.Turtle()
t.speed(-1)

# This controls Canvas width and height. Feel free to change it according to your needs
            # width⬇,height⬇ 
turtle.screensize(2000, 1000)

'''
                        Keys and their Functions:
        
        Set Pen color(randomly): 'm'
        Set Screen background color(randomly): 'n',
        
        Set Turtle Direction:
        rotate 90° towards north:'Up direction key',
        rotate 90° towards sout: 'Down direction key',
        rotate 90° towards east: 'Right direction key',
        rotate 90° towards west: 'Left direction key',
        rotate 5° towards left: 'a',
        rotate 5° towards right: 'd',

        Drawing the line:
        Draw a line of 50 units forwards: 'w',
        Draw a line of 50 units backwards: 's',
        
        Visibility of turtle: 
        Hide Turle: '0',
        Show Turtle: '1'

        Clear the canvas and reset position of cursor: 'c' 

        *** You have to drag pen while using mouse to draw *** 
        *** Left Click anywhere on the screen to move the pen to that point while drawing(pendown) ***(*See line no. 110)
        *** Right Click anywhere on the screen to move the pen to that point without drawing(penup) ***
'''

# Setting up the Direction of pen :


def direction(num):
    t.seth(num)
    t.screen.update()


def rotate(num):
    t.lt(num)

# Drawing with keyboard:

def draw(num):
    t.fd(num)

# Drawing with mouse:

def dragging(x, y):
    t.ondrag(None)
    t.setheading(t.towards(x, y))
    t.goto(x, y)
    t.ondrag(dragging)


def pendown_and_move(x, y):
    t.seth(t.towards(x, y))
    t.goto(x, y)


def penup_and_move(x, y):
    t.seth(t.towards(x, y))
    t.penup()
    t.goto(x, y)
    t.pendown()


# Change color of pen and background of screen:


def set_pen_color():
    pen_colors = ['white', "red", 'yellow', 'chocolate',
                  'black', 'blue', 'green', 'turquoise', "violet"]
    t.pencolor(random.choice(pen_colors))


def set_bg_color():
    bg_colors = ['blue', 'black', 'green', "violet",
                 'white', "red", 'yellow', 'turquoise', 'chocolate', ]
    Screen().bgcolor(random.choice(bg_colors))


listen()
onkeypress(lambda: direction(90), "Up")
onkeypress(lambda: direction(270), "Down")
onkeypress(lambda: direction(180), "Left")
onkeypress(lambda: direction(0), "Right")
onkeypress(lambda: rotate(5), 'a')
onkeypress(lambda: rotate(-5), "d")
onkeypress(lambda: draw(50), 'w')
onkeypress(lambda: draw(-50), 's')
onkeypress(t.hideturtle, '0')
onkeypress(t.showturtle, '1')
onkeypress(t.reset, 'c')
onkeypress(set_pen_color, 'm')
onkeypress(set_bg_color, 'n')
onscreenclick(penup_and_move, btn=3)

# Comment out only one of the below two statements. Using both at a time is little buggy. The second statement is commented out by default.

t.ondrag(dragging) # With this you can draw by dragging pen as your wish
# onscreenclick(pendown_and_move, btn=1) # This will draw a line from current pen position to the clicked point postion


turtle.done()