var = 'Valor'

def func():
    print(var)

def func2():
    global var # agora a variável está no escopo global do programa (não é uma boa prática)
    var = 'Outro valor'
    print(var)

func()
func2()

print(var)