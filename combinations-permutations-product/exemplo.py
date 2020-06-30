import itertools

pessoas = ['João', 'Maria', 'Bob', 'Fernanda', 'Eduardo', 'Rosa']

# com combinations, a ordem NÃO importa (ex: João e Maria é a mesma coisa que Maria e João)

for grupo in itertools.combinations(pessoas, 2):
    print(grupo)