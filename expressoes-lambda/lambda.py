"""
func = lambda x, y: x + y

print(func(2, 3))
"""

produtos = [
    ['Celular', 1100.00],
    ['TV', 1900.00],
    ['Microondas', 290.00],
    ['Ventilador', 120.00],
    ['Liquidificador', 100.00]
]

def ordenar(item):
    return item[1]

produtos.sort(key = ordenar, reverse = True)
print(produtos)