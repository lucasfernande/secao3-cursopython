import dados

"""
newList = list(map(lambda x: x * 2, dados.lista))

print(dados.lista)
print(newList)
"""

precos = list(map(lambda p: p['preco'], dados.produtos))

for preco in precos:
    print(preco)