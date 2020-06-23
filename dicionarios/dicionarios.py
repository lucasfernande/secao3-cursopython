"""
dicio = {'nomedaChave':'valor da chave'}
dicio['outra_chave'] = 'valor da outra chave'

print(dicio)
print(dicio['nomedaChave'])
"""

dicio = dict(chave = 'valor da chave', chave2 = 'valor da chave2')

"""
print(dicio)
print(dicio.get('chave'))

dicio.update({'chave':'outro valor'}) # atualizando uma chave
dicio.update({'chave3':'valor da chave3'}) # adicionando uma nova chave

print(dicio)

del dicio['chave3'] # deletando uma chave
print(dicio)

"""

"""
print('chave2' in dicio) 
print('chave2' in dicio.keys()) # checando se chave2 existe nas chaves de dicio
print('valor da chave' in dicio.values()) # checando se valor da chave existe nos valores de dicio

print(len(dicio))
"""

for key in dicio.keys(): # iterando sobre as chaves
    print(key)

for value in dicio.values(): # iterando sobre os valores
    print(value)

for items in dicio.items(): # iterando sobre chaves e valores
    print(items)