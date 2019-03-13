import turtle as t         #alias



while True:
    lettera = input("Inserisci lettera: ")
    if(lettera == "f"):
        t.forward(50)
    elif (lettera == "l"):
        t.left(90)
    elif (lettera == "r"):
        t.right(90)
    elif (lettera == "b"):
        t.back(50)
t.done()