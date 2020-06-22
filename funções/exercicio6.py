def executar(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def ola(nome):
    return f'Olá, {nome}'

def saudacao(saudacao, nome):
    return f'{saudacao}, {nome}'

exec = executar(ola, 'Lucas')
exec2 = executar(saudacao, 'Bom dia', 'Lucas')

print(exec)
print(exec2)