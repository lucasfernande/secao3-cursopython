import dados

"""
newList = list(map(lambda x: x * 2, dados.lista))

print(dados.lista)
print(newList)
"""

def reajuste(p):
    p['preco'] = round(p['preco'] * 1.05, 2)
    return p

precos = map(reajuste, dados.produtos)

for p in precos:
    print(p)