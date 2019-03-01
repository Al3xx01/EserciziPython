import turtle as t         #alias

a = 0
b = 1

braccia = int(raw_input("Inserisci il numero di braccia: "))

while True:
    if(braccia > 0):
        t.forward(b)       #avanti
        a, b = b, a + b    #serie fibonacci
        t.left(90)         #gira a sinistra di 90 gradi
        braccia = braccia - 1
    else:
        break

t.done()