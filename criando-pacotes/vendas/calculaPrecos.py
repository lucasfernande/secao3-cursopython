def reajusteAumenta(preco, porcent):
    r = preco + (preco * (porcent / 100))
    return r

def reajusteAbaixa(preco, porcent):
    r = preco - (preco * (porcent / 100))
    return r