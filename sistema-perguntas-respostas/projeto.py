perguntas = {
    'Pergunta 1' : {
        'pergunta' : 'Quanto é 6x8?',
        'respostas' : {'a' : '40', 'b' : '45', 'c' : '48', 'd' : '36'},
        'resp_certa' : 'c',
    },
    'Pergunta 2' : {
        'pergunta' : 'Em que ano foi promulgada a Constituição da República Federativa do Brasil?' ,
        'respostas' : {'a' : '1984', 'b' : '1985', 'c' : '1990', 'd' : '1988'},
        'resp_certa' : 'd',
    },
    'Pergunta 3' : {
        'pergunta' : 'Qual o maior país do Mundo' ,
        'respostas' : {'a' : 'Rússia', 'b' : 'Brasil', 'c' : 'Canadá' ,'d' : 'Estados Unidos'},
        'resp_certa' : 'a',
    },
}
acertos = 0
erros = 0


for chavePergunta, perguntaValor in perguntas.items():
    print()
    print(f'{chavePergunta} : {perguntaValor["pergunta"]}')

    for chaveResposta, respostaValor in perguntaValor['respostas'].items():
        print(f'[{chaveResposta}] : {respostaValor}')

    respostaUsuario = input('Digite a alternativa correta: ')

    if respostaUsuario == perguntaValor['resp_certa']:
        print()
        print('Resposta correta')
        acertos += 1
    else:
        print()
        print('Resposta incorreta')
        erros += 1

print()
perc = acertos / len(perguntas) * 100
print(f'{perc:.1f}% de acerto')