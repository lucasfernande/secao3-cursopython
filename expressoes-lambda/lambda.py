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

produtos.sort(key = lambda item: item[1], reverse = True)
print(produtos)