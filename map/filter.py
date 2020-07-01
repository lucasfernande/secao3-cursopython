import dados

# filtroComp = [x for x in dados.lista if x > 5] list comprehension
# filtro = filter(lambda x: x > 4, dados.lista)
# print(list(filtro))

"""
def filtra(prod):
    if prod['preco'] > 50:
        return True

filtroProduto = filter(filtra, dados.produtos)

for prod in filtroProduto:
    print(prod)
"""

def maiorIdade(pessoa):
    if pessoa['idade'] >= 18:
        return True

filtroIdade = filter(maiorIdade, dados.pessoas)

for pessoa in filtroIdade:
    print(pessoa)