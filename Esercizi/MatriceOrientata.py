# Cognome nome: Casale Alex
# Classe: 4A^ROB

import random

dim = 5          #dimensione matrice

m = [[0]*dim]*dim       #Inizializzo la matrice con tutte le celle a 0
print("Matrice (1° fase): ")
print (m)

for r in range(dim):        #Ciclo for per scorrere le righe
    for c in range(dim):        #Ciclo for per scorrere le colonne
        if r!=c:
            m[r][c] =int(random.random()*10)        #riempo la matrice con un numero random da 0 a 10
            m[c][r] = m[r][c]

print("\nMatrice (2° fase): ")
print(m)
