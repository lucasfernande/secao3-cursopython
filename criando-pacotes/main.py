
from vendas import calculaPrecos

preco = 49.90

precoReajuste = calculaPrecos.reajusteAumenta(preco, 10)
print(calculaPrecos.formata(precoReajuste))

precoReducao = calculaPrecos.reajusteAbaixa(preco, 10)
print(calculaPrecos.formata(precoReducao))

