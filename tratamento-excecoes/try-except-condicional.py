def conversorNumero(var):
    try:
        var = int(var)
        return var
    except ValueError:
        try:
            var = float(var)
            return var
        except ValueError:
            pass

num = conversorNumero(input('Digite um número: '))

if num is not None:
    print(num * 5)
else:
    print('Digite apenas números')