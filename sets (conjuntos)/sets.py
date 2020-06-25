"""
set = {1, 2, 3, 4, 5, 6, 7}

set.add(8)
set.add(9)
set.add(10)

for valor in set:
    print(valor)

set.discard(10)
set.discard(9)

print(set)

set.update([9, 10, 11, 12])

print(set)
"""
"""
lista = [1, 2, 3, 3, 3, 4, 2, 2, 5, 5, 6, 7, 7, 7, 8, 9, 9, 10]

lista = set(lista) # convertendo para set
lista = list(lista) # voltando para lista

print(lista)
"""

set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3, 4, 5, 6, 7, 8,}

set3 = set1 | set2
print(set3)
