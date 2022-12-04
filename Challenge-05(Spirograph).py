import turtle as t
import random

kachuwa = t.Turtle()
t.colormode(255)

def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color = (red, green, blue)
    return color

kachuwa.speed("fastest")
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        kachuwa.color(random_color())
        kachuwa.circle(100)
        kachuwa.setheading(kachuwa.heading() +size_of_gap)
draw_spirograph(5)

my_screen = t.Screen()
my_screen.exitonclick()

