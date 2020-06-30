import itertools

pessoas = ['João', 'Maria', 'Bob', 'Fernanda', 'Eduardo', 'Rosa']

# com product, terá a possibilidade de ter valores repetidos (ex: João e João)

for grupo in itertools.product(pessoas, repeat = 2):
    print(grupo)