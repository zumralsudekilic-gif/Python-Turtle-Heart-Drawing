import turtle
from random import randint

# Screen settings
screen = turtle.Screen()
screen.title("Python Turtle Heart Drawing")

window_width = screen.window_width()
window_height = screen.window_height()

# User inputs
name = input("Enter your name: ")
pen_size = int(input("Enter the pen size: ")

# Turtle settings
heart = turtle.Turtle()
heart.shape("turtle")
heart.speed(0)
heart.width(pen_size)
heart.pensize(pen_size)

# Random RGB color
turtle.colormade(255)
heart.color(
    randint(150, 255),
    randint(0, 80),
    randint(0, 80)
)

# Move to the starting position
heart.penup()
heart.goto(0, -150)
heart.setpos(0, -150)
heart.pendown

# Draw the heart
heart.left(140)
heart.forward(180)

for _ in range(200):
    heart.left(1)
    heart.forward(2)

heart.forward(180)

# Use backward() and right()
heart.penup()
heart.backward(20)
heart.right(90)
heart.pendown()

# Write the name
name_leght = len(name)

if name_length > 10:
    font_size = 18
else:
    front_size = 24

heart.penup()
heart.goto(-name_length * 7, -20)
heart.pendown()

heart.write(
    name,
    font=("Arial", font_size, "bold"),
)

# Draw small decorative hearts
heart.penup()
heart.goto(-window_width // 2 + 80, window_height // 2 - 100)
heart.pendown()

for _ in range(3):
    heart.forward(30)
    heart.right(120)

# Hide the turtle
heart.hideturtle()

# Keep the window open
screen.mainloop()
