string = '0123456789012345678901234567890123456789012345678901234567890123456789'
n = 10
conjuntos = [string[i : i + n] for i in range(0, len(string), n)]
retorno = '.'.join(conjuntos)
print(conjuntos)
print(retorno)

