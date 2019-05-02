# Cognome nome: Casale Alex
# Classe: 4A^ROB

m = [[0, 0, 0, 1, 0], [1, 2, 1, 0, 1], [0, 1, 5, 1, 0], [1, 0, 0, 0, 0], [0, 1, 0, 0, 0]]

n = -1

for i in m:

    cnt = 0
    n = n + 1
    neighbourNodes = []

    for j in i:
        if (j != 0):
            neighbourNodes.append(cnt)
        cnt = cnt + 1

    print("Nodo: " + str(n) + " -> Posizione: " + str(neighbourNodes))
