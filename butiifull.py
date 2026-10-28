import turtle

# Screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(900, 900)
screen.title("Blooming Tree")

# Turtle
t = turtle.Turtle()
t.speed(550)
t.left(90)
t.penup()
t.goto(0, -300)
t.pendown()
t.color("brown")
t.hideturtle()

# Tree Function
def tree(i):
    if i < 10:
        return

    t.pensize(i / 10)

    # Draw branch
    t.forward(i)

    # Flower
    t.color("pink")
    t.dot(4)

    # Back to branch color
    t.color("brown")

    # Left Branch
    t.left(20)
    tree(i * 4 / 5)

    # Right Branch
    t.right(40)
    tree(i * 4 / 5)

    # Return to original direction
    t.left(20)

    # Go back
    t.backward(i)

# Start Drawing
tree(100)

turtle.done()