"""
file = open('in.txt', 'w+') # w+ significa leitura e escrita

file.write('Linha\n')
file.write('Outra linha\n')
file.write('Outra linha')

file.seek(0, 0) # movendo o cursor para o topo do arquivo para poder ler o arquivo
print('Lendo arquivo: ')
print(file.read())
print()

file.seek(0, 0)
print(file.readline(), end='') # end para não quebrar linha
print(file.readline(), end='')
print(file.readline())

file.seek(0, 0)
for line in file.readlines():
    print(line, end='')

file.close()
"""

with open('in.txt', 'w+') as file:
    file.write('Linha\n')
    file.write('Outra\n')
    file.write('Outra Linha')

    file.seek(0, 0)
    print(file.read())