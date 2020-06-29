import sys
import time
"""
def gerador():
    for n in range(100):
        yield n
        time.sleep(0.1) # pausando o interpretador


gera = gerador()

for v in gera:
    print(v)
"""

# comparando os tamanhos da lista e gerador

lista1 = [x for x in range(1000)]
lista2 = (x for x in range(1000))
print(sys.getsizeof(lista1))
print(sys.getsizeof(lista2))
