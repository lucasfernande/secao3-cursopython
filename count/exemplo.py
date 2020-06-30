from itertools import count

contador = count(start = 10, step = -1)

# start = começo, step = de quanto em quanto ele vai pular

for v in contador:
    print(v)
    if v <= 0:
        break


