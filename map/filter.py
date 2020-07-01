import dados

# filtroComp = [x for x in dados.lista if x > 5] list comprehension
# filtro = filter(lambda x: x > 4, dados.lista)
# print(list(filtro))

filtroProduto = filter(lambda p: p['preco'] > 45, dados.produtos)

for prod in filtroProduto:
    print(prod)