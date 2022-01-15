from random import *
from turtle import *


setup(800, 600)
tab_horiz = [randint(0,1) for _ in range (30)]
tab_verti = [randint(0,1) for _ in range (40)]
print(tab_horiz)
print(tab_verti)

speed(0)

indice = 0
y_coord = 300
x_coord = -400


while y_coord >= -280:
    up()
    goto(-400,y_coord)
    down()

    if tab_horiz[indice] == 0 :
        for _ in range (20):
            forward(20)
            up()
            forward(20)
            down()
    else :
        for _ in range (20):
            up()
            forward(20)
            down()
            forward(20)
    y_coord -= 20
    indice += 1

indice = 0
y_coord = 300
x_coord = -400

setheading(270)

while x_coord <= 380:
    up()
    goto(x_coord,300)
    down()

    if tab_verti[indice] == 0 :
        for _ in range (15):
            forward(20)
            up()
            forward(20)
            down()
    else :
        for _ in range (15):
            up()
            forward(20)
            down()
            forward(20)
    x_coord += 20
    indice += 1

exitonclick()