def divide(n1, n2):
    if n2 == 0:
        raise ValueError('O número não pode ser dividido por Zero')
    return n1 / n2

n1 = 2
n2 = 0

try:
    print(divide(n1, n2))
except ValueError as error:
    print(f'Não é possível dividir {n1} por zero')
    print('Log: ', error)