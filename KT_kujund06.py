# Turtle KT 06
# Matis Russi
# IT-21
# 14.03.2022

# Moodulid

import turtle

# Akna seaded

aken = turtle.Screen()
aken.setup(500,500)
aken.title("Kujund 06 - Matis Russi")

# Muutujad

turn = 4

# Kujund

kk = turtle.Turtle()
kk.right(90)

for i in range(turn):
    kk.left(90)
    kk.forward(100)
    kk.left(90)
    kk.forward(50)
    kk.left(90)
    kk.forward(150)
    
turtle.exitonclick()
