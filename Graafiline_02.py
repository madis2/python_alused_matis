# Graafiline 02
# Matis Russi
# IT-21
# 14.03.2022

# Moodulid

import turtle

# Viisnurk

aken = turtle.Screen()
aken.setup(300,300)
aken.title("Viisnurk - Matis Russi")

turn = 5
nn = turtle.Turtle()
nn.left(180)
for i in range(turn):
    nn.forward(100)
    nn.left(144)
    
# Võrdkülgne kolmnurk

def joonista_kolmnurk(a,varv):
    kk = turtle.Turtle()
    for i in range(0,3):
        kk.color(varv)
        kk.forward(a)
        kk.left(120)
    

joonista_kolmnurk(100,'red')

turtle.exitonclick()