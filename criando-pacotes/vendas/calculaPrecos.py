def reajusteAumenta(preco, porcent, formata = True):
    r = preco + (preco * (porcent / 100))
    return r

def reajusteAbaixa(preco, porcent, formata = True):
    r = preco - (preco * (porcent / 100))
    return r

def formata(preco):
    return f'R$ {preco:.2f}'.replace('.', ',')