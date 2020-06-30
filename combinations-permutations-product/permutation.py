import itertools

pessoas = ['João', 'Maria', 'Bob', 'Fernanda', 'Eduardo', 'Rosa']

# com permutation, a ordem importa (ex: João e Maria não é considerado a mesma coisa que Maria e João)

for grupo in itertools.permutations(pessoas, 2):
    print(grupo)