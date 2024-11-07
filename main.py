import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)

Jonny = Turtle()
print(Jonny)
Jonny.ht()
Jonny.pensize(1)
Jonny.speed(0)
Jonny.shape('turtle')
Jonny.color('medium sea green')
Jonny.teleport(-50,100)

def change_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    new_color = (r, g, b)
    Jonny.color(new_color)

def print_figure (corners):
    for number in range(corners):
        Jonny.forward(100)
        Jonny.right(360/corners)

def print_sequence (polygon):
    for number_corners in range(polygon):
        if number_corners >= 3:
            print_figure(number_corners)
            change_color()

def random_walk(distance):
    for _ in range(distance):
        random_way = random.choice([0, 90, 180, 270])
        Jonny.setheading(random_way)
        Jonny.forward(30)
        change_color()

def draw_circle (step):
    for degree in range(int(round(360 / step))+1):
        Jonny.circle(100)
        Jonny.setheading(degree * step)
        change_color()

print_sequence(12)

random_walk(100)

draw_circle(2)








my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

