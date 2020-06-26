"""
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

lista2 = [valor for valor in lista]

print(lista2)

listaDobro = [valor * 2 for valor in lista]
print(listaDobro)
"""

"""
nomes = ['lucas', 'maria', 'alex']
conv = [nome.replace(nome[0], nome[0].upper()) for nome in nomes]

print(conv)
"""

lista = list(range(100))
filtro =  [valor for valor in lista if valor % 2 == 0]
print(filtro)