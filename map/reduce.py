import functools
import dados

"""
somaLista = functools.reduce(lambda ac, i: i + ac, dados.lista, 0)

print(somaLista)
"""

somaPrecos = functools.reduce(lambda ac, p: p['preco'] + ac, dados.produtos, 0)

print(round(somaPrecos / len(dados.produtos), 2))