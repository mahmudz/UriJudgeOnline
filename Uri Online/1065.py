# -*- coding: utf-8 -*-
numeros = []
aux = 0
for i in range(5):
    numeros.append(int(input()))
    if numeros[i] % 2 == 0:
        aux +=1
print("%d valores pares" %aux)
