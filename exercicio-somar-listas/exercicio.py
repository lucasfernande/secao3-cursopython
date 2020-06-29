listaA = [1, 2, 3, 4, 5, 6, 7]
listaB = [1, 2, 3, 4]

"""
for i in range(len(listaB)):
    listaSoma.append(listaB[i] + listaA[i])

print(listaSoma)
"""
listaSoma = [x + y for x, y in zip(listaA, listaB)]
print(listaSoma)