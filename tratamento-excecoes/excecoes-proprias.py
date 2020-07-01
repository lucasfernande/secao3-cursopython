def divide(n1, n2):
    if n2 == 0:
        raise ValueError('O número não pode ser dividido por Zero')
    return n1 / n2

print(divide(2, 0))