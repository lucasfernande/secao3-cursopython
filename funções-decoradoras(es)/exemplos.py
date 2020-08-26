"""""
def fala_oi():
    print('oi')

var = fala_oi

print(type(var))
var()
"""""

def master():
    def slave():
        print('oi')
    return slave

var = master()

var()
