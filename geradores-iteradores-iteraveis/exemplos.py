import sys
import time

def gerador():
    for n in range(100):
        yield n
        time.sleep(0.1) # pausando o interpretador


gera = gerador()

for v in gera:
    print(v)