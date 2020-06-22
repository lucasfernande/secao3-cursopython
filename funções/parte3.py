def func(*args, **kwargs):
    print(args)
    print(args[0]) # primeiro valor
    print(args[-1]) # último valor
    print(len(args)) # quantidade de valores
    
    nome = kwargs.get('nome') # checando se algum kwarg nome foi enviado
    print(nome)

    idade = kwargs.get('idade') # falso
    print(idade)

lista = [1, 2, 3, 4, 5]
lista2 = [6, 7, 8, 9, 10]
func(*lista, *lista2, nome = 'Lucas', sobrenome = 'Fernandes')


"""
lista = [1, 2, 3, 4, 5]
n1, n2, *n = lista
print(n1, n2, n)
print(*lista, sep=', ')
"""