import turtle
import random

# ------------------ Setup Canvas ------------------
screen = turtle.Screen()
screen.bgcolor("#EEE1DD")
screen.setup(width=900, height=900)
screen.title("Fluid Recursive Growth (Biological Ink)")
screen.tracer(0)

# ------------------ Setup Turtle ------------------
t = turtle.Turtle()
t.speed(0)
t.left(90)
t.penup()
t.goto(0, -350)
t.pendown()
t.hideturtle()

# ------------------ Tree Function ------------------
def grow(t, length, thickness):
    if length < 8:
        return

    t.pensize(thickness)

    color_val = int(255 * (thickness / 15))
    color_val = max(min(color_val, 200), 20)
    color_hex = f"#{color_val:02x}{color_val:02x}{color_val:02x}"

    t.pencolor(color_hex)
    t.forward(length)

    pos = t.pos()
    heading = t.heading()

    # Left branch
    t.left(random.randint(15, 30))
    grow(t, length * random.uniform(0.70, 0.80), thickness * 0.7)

    t.penup()
    t.goto(pos)
    t.setheading(heading)
    t.pendown()

    # Right branch
    t.right(random.randint(15, 30))
    grow(t, length * random.uniform(0.70, 0.80), thickness * 0.7)

    t.penup()
    t.goto(pos)
    t.setheading(heading)
    t.pendown()

# ------------------ Start Drawing ------------------
grow(t, 120, 15)

screen.update()
turtle.done()