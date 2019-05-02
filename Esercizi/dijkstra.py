import math
graph = [
    [0,3,0,4],
    [3,0,1,5],
    [0,1,0,2],
    [4,5,2,0]
]

source = 0
nodeNumber = len(graph)                                        #Numero di nodi

labelList = [math.inf for i in range(nodeNumber)]              #Lista delle distanze
labelList[source] = 0                                          #Distanza del nodo iniziale

unexploredNodes = [i for i in range(nodeNumber)]               #Nodi da esplorare

while len(unexploredNodes)>0:
    minLabel = min([labelList[node] for node in unexploredNodes])                                  #Valore minimo

    for i in unexploredNodes:
        if labelList[i] == minLabel:
            currentNode = i  #Posizione del valore minimo nel grafo
        else:
            break

    unexploredNodes.remove(currentNode)                         #Rimuovo il nodo corrente

    for neighbourNode,weight in enumerate(graph[currentNode]):
        if weight>0:
            distance = labelList[currentNode] + weight
            if distance<labelList[neighbourNode]:
                labelList[neighbourNode] = distance

print(graph)
print(labelList)


