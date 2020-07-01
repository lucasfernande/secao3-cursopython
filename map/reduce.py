import functools
import dados

somaLista = functools.reduce(lambda ac, i: i + ac, dados.lista, 0)

print(somaLista)
