import turtle as t
import random

kachuwa = t.Turtle()

colours = ["black", "white", "gray", "silver", "maroon", "red", "purple", "fushsia", "green", "lime", "olive", "yellow", "navy", "blue", "teal", "aqua"]
directions = [0, 90, 180, 270]
kachuwa.pensize(15)
kachuwa.speed("fastest")

for _ in range(1000):
    kachuwa.color(random.choice(colours))
    kachuwa.forward(50)
    kachuwa.setheading(random.choice(directions))


