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
