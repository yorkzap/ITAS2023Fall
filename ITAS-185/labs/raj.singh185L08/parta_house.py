"""
Course: ITAS 185 - Introduction to Programming
Lab08: Simple House Drawing with Turtle
Description:
    This Python file uses the 'turtle' module to create a drawing of a simple house centered on the canvas.
    The house includes a box-like structure, a roof, a window, and a door.
    At least one part of the house is filled with color.
    Additionally, a creative element like a chimney, birds, or a tree may be added for added visual appeal.
    Customize colors, sizes, and details to create a unique house drawing.
"""

import turtle

# Set up the turtle screen with a size of 800x800 pixels.
screen = turtle.Screen()
screen.setup(width=800, height=800)

# Create a turtle object.
t = turtle.Turtle()
t.speed(10)


def draw_rectangle(x, y, width, height, color):
    """Draw a rectangle."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()


def draw_circle(x, y, radius, color):
    """Draw a circle."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


def draw_triangle(x, y, side_length, color):
    """Draw a triangle."""
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(3):
        t.forward(side_length)
        t.left(120)
    t.end_fill()


def draw_house():
    """Draw a house."""
    # Draw the house (box-like shape).
    draw_rectangle(-200, -150, 200, 200, "grey")

    # Draw the roof (triangle).
    draw_triangle(-200, 50, 200, "red")

    # Draw the door (rectangle).
    draw_rectangle(-125, -150, 50, 100, "blue")

    # Draw the window (square).
    draw_rectangle(-60, -20, 50, 50, "orange")

    # Draw a tree outside the house.
    draw_rectangle(150, -150, 30, 90, "brown")

    # Draw the tree leaves (circle).
    draw_circle(165, -80, 80, "green")

    # Hide the turtle and display the drawing.
    t.hideturtle()


# Call the draw_house function to draw the house.
draw_house()

# Use exitonclick() to keep the window open until clicked.
screen.exitonclick()
