try:
    a = []
    print(a)
except NameError as erro:
    print('Erro: ', erro)
except (IndexError, KeyError) as erro:
    print('Erro de índice ou chave: ', erro)
except Exception as erro:
    print('Ocorreu um erro inesperado')
else: # este bloco será executado sempre que o bloco try ser executado sem exceções
    print('Código executado com sucesso')
finally: # este bloco SEMPRE será executado
    print('Final')
