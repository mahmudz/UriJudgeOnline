# -*- coding: utf-8 -*-
numeros = []
aux = 0
for i in range(6):
    numeros.append(float(input()))
    if numeros[i] > 0:
        aux +=1
print("%d valores positivos" %aux)