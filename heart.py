import turtle
import math
import time

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(800, 800)
screen.title("Beating Heart")

t = turtle.Turtle()
t.speed(0)
t.color("red")
t.pensize(3)
t.hideturtle()

screen.tracer(0)

while True:
    for scale in [10, 11, 12, 13, 14, 13, 12, 11]:
        t.clear()
        t.penup()

        for i in range(361):
            a = math.radians(i)

            x = 16 * math.sin(a) ** 3
            y = (13 * math.cos(a)
                 - 5 * math.cos(2 * a)
                 - 2 * math.cos(3 * a)
                 - math.cos(4 * a))

            x *= scale
            y *= scale

            if i == 0:
                t.goto(x, y)
                t.pendown()
            else:
                t.goto(x, y)

        screen.update()
        time.sleep(0.08)