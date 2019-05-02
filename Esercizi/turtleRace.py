import turtle as t
import random

lista = []
cnt = 0
nTurtles = 0

def setup():
    posX = -300
    posY = 300
    nTurtles = 5


    t.setup(700, 700)
    for i in range(0,nTurtles):
        lista.append(t.Turtle())
        lista[i].penup()
        posY -= 50
        lista[i].setpos(posX, posY)
        lista[i].pendown()
        turtle = random.randrange(0, nTurtles)
        if turtle == 0:
            lista[i].color("red")
        elif turtle == 1:
            lista[i].color("blue")



setup()
while True:

    for k in lista:
        if(k.xcor() +50 < 300):
            k.forward(random.randrange(10, 50))
            cnt = cnt + 1

        else:
            print(str((cnt % 5) + 1) + " ha vinto")
            t.done()
            break


