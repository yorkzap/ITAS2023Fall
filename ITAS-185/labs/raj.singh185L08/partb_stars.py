"""
Course: ITAS 185 - Introduction to Programming
Lab08: Star generator using Turtle module

Description:
    This Python script uses the 'turtle' module to generate a star shape on the canvas.
    The user is prompted to enter the number of points on the star, which should be an odd number between 5 and 101 (default is 5).
    The script draws a star with the specified number of points on the canvas.
    The star is filled with a yellow color, and its outline is in black.
    The window closes when clicked.
"""

import turtle

# Set up the turtle screen with a size of 800x800 pixels.
window = turtle.Screen()
window.setup(width=800, height=800)

# Ask the user for the number of points on the star
num_points_input = input("Enter an odd number between 5 and 101 (5 by default): ")
num_points = int(num_points_input) if len(num_points_input) != 0 else 5

# Confirm if the selected number is odd
if num_points % 2 != 0:
    # Create a turtle object
    star = turtle.Turtle()
    star.speed(0)

    # Set fill color and pen color
    star.fillcolor('yellow')
    star.pencolor('black')

    # Set the initial position
    star.penup()
    star.goto(-200, 0)
    star.pendown()

    # Set the turn angle
    turn_angle = 180 - (180 / num_points)

    # Draw the star
    star.begin_fill()
    for _ in range(num_points):
        star.forward(400)
        star.right(turn_angle)
    star.end_fill()

# Close the window when clicked
window.exitonclick()
