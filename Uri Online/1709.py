# -*- coding: utf-8 -*-
N = int(input())
cartas = []
for i in range(1, N+1):
    cartas.append(i)
qtd_embaralhadas = 0
embaralhado = False
metade = int(len(cartas)/2)
C1 = list([0]*metade)
C2 = list([0]*metade)
while embaralhado == False:
    aux = 0
    for i in range(len(cartas)):
        if i < metade:
            C1[i] = cartas[i]
        else:
            C2[aux] = cartas[i]
            aux += 1
    aux = 0
    for i in range(len(cartas)):
        if i % 2 == 0:
            cartas[i] = C2[aux]
        else:
            cartas[i] = C1[aux]
            aux += 1
    embaralhado = True
    for i in range (len(cartas)-1):
        if cartas[i] > cartas[i+1]:
            embaralhado = False
            break
    qtd_embaralhadas += 1

print(qtd_embaralhadas)