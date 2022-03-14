# Graafiline 01
# Matis Russi
# IT-21
# 14.03.2022

import turtle
import random

# Akna seaded

aken = turtle.Screen()
aken.setup(300,300)
aken.title("Ülesanne 01 - Matis Russi")

# Muutujad

colors = ('red','blue','green','orange','yellow')
turn = 0
spikes = 8
size = 10

# Hakkan nooli genereerima

for i in range(spikes):
    kk = turtle.Turtle()
    kk.color(random.choice(colors))
    kk.left(turn)
    kk.forward(100)
    turn += 45

turtle.exitonclick()