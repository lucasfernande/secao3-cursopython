from itertools import count

contador = count(start = 5, step = 2)

# start = começo, step = de quanto em quanto ele vai pular

for v in contador:
    print(v)
    if v >= 15:
        break


