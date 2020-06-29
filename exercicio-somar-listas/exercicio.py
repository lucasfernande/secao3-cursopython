listaA = [1, 2, 3, 4, 5, 6, 7]
listaB = [1, 2, 3, 4]

listaSoma = []
for i in range(len(listaB)):
    listaSoma.append(listaB[i] + listaA[i])

print(listaSoma)