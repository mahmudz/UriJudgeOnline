import random

numeros = []
for i in range(15):
    aux = random.randint(10, 100)
    while aux in numeros:
        aux = random.randint(10, 100)
    numeros.append(aux)

numeros.sort()
print(numeros)

