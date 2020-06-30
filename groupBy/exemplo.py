import itertools

notas = [
    {'nome' : 'Lucas', 'nota' : 'A'},
    {'nome' : 'João', 'nota' : 'B'},
    {'nome' : 'Maria', 'nota' : 'D'},
    {'nome' : 'Fernanda', 'nota' : 'A'},
    {'nome' : 'Eduardo', 'nota' : 'C'},
    {'nome' : 'Jéssica', 'nota' : 'B'},
    {'nome' : 'André', 'nota' : 'D'},
    {'nome' : 'Fabrício', 'nota' : 'B'}
]

ordena = lambda item: item['nota'] # ordenando a lista por nota

notas.sort(key = ordena)
notasAgrupadas = itertools.groupby(notas, ordena)

for grupos, alunos in notasAgrupadas:
    print(f'Nota: {grupos}')
    for aluno in alunos:
        print(f"\t{aluno['nome']}")
    print()