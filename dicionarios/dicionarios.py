"""
dicio = {'nomedaChave':'valor da chave'}
dicio['outra_chave'] = 'valor da outra chave'

print(dicio)
print(dicio['nomedaChave'])
"""

dicio = dict(chave = 'valor da chave', chave2 = 'valor da chave2')
print(dicio)
print(dicio.get('chave'))