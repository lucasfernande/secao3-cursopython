from itertools import count

contador = count()

# start = começo, step = de quanto em quanto ele vai pular
lista = ['Luiz', 'Maria', 'João', 'Eduardo']
lista = zip(contador, lista)

print(list(lista))



"""
for v in contador:
    print(v)
    if v <= 0:
        break
"""

