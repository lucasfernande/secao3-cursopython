from itertools import zip_longest

capitais = ['São Paulo', 'Salvador', 'Curitiba', 'Goiânia', 'Manaus', 'Rio Branco', 'Porto Alegre']

estados = ['SP', 'BA', 'PA', 'GO', 'AM']

cidades_estados = zip_longest(estados, capitais) # o zip longest irá preencher o estado com none

print(list(cidades_estados))