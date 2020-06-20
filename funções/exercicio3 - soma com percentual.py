def somar(num, perc):
    soma = num / 100 * perc
    return num + soma

num = int(input('Digite um número inteiro: '))
perc = int(input('Digite o percentual a ser somado: '))

result = somar(num, perc)
print(result)
