import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle object
heart = turtle.Turtle()
heart.shape("turtle")
heart.color("red")
heart.speed(2)

#
heart.begin_fill()
heart.fillcolor("red")
heart.left(140)
heart.forward(224)
for _ in range(200):
    heart.right(1)
    heart.forward(2)
heart.left(120)
for _ in range(200):
    heart.right(1)
    heart.forward(2)
heart.forward(224)
heart.end_fill()

# Close the window on the click
screen.exitonclick()
