try:
    a = []
    print(a[1])
except NameError as erro:
    print('Erro: ', erro)
except (IndexError, KeyError) as erro:
    print('Erro de índice ou chave: ', erro)
except Exception as erro:
    print('Ocorreu um erro inesperado')