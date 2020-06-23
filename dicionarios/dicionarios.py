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

print('chave2' in dicio)
print('chave2' in dicio.keys())
print('valor da chave' in dicio.values())

print(len(dicio))