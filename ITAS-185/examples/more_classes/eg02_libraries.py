import turtle

turt = turtle.Turtle()
win = turtle.Screen()

win.setup(800, 800)
win.bgcolor('ivory')


# Create a turtle object
turt = turtle.Turtle()

# Set the turtle's speed
turt.speed(1)  # You can adjust the speed as needed


# Draw the longer tower-like shape with a wider egg-like top
turt.forward(150)  # Base
turt.left(90)
turt.forward(80)  # Vertical line

# Draw the wider egg-like top
turt.circle(100, 180)  # 100 is the radius, and 180 is the extent (half circle)

# Continue drawing the tower
turt.forward(80) 
turt.left(90)
turt.forward(150)
turt.left(90)
turt.forward(80) 
