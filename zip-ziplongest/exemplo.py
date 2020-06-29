from itertools import zip_longest, count

indice = count()
capitais = ['São Paulo', 'Salvador', 'Curitiba', 'Goiânia', 'Manaus', 'Rio Branco', 'Porto Alegre']
estados = ['SP', 'BA', 'PA', 'GO', 'AM']

cidades_estados = zip(indice, estados, capitais)

# o zip longest irá preencher o estado com none

for ind, cid, est in cidades_estados:
    print(ind, cid, est)
