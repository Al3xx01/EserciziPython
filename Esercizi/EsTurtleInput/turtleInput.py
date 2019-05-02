#Casale Alex 13-03-2019
import turtle as t         #alias

passo = 50
angolo = 90


comandi = input("Inserisci la stringa: ")

for k in comandi:

    if(k == 'f'):
        t.forward(passo)
    elif (k == 'l'):
        t.left(angolo)
    elif (k == 'r'):
        t.right(angolo)
    elif (k == 'b'):
         t.back(passo)
    else:
         print("Comando inesistente [commands: f, b, r, l]")

t.done()