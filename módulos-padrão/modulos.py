"""
import sys
print(sys.platform) # método que mostra o OS do usuário
"""
"""
from sys import platform as so # importando apenas uma função e dando um apelido
print(so)
"""

from random import * # importando tudo do modulo

for i in range(10):
    print(random.randint(0, 10))