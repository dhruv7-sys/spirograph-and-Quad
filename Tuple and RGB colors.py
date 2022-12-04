import turtle as t
import random

kachuwa = t.Turtle()
t.colormode(255)

def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    random_color = (red, green, blue)
    return random_color


directions = [0, 90, 180, 270]
kachuwa.pensize(15)
kachuwa.speed("fast")

for _ in range(100):
    kachuwa.color(random_color())
    kachuwa.forward(50)
    kachuwa.setheading(random.choice(directions))

