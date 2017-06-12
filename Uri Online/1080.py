# -*- coding: utf-8 -*-
lista = list([0]*100)
maior = -1
posicao = -1
for i in range(100):
    lista[i] = int(input())
    if i == 0:
        maior = lista[i]
        posicao = i
    elif lista[i] > maior:
        maior = lista[i]
        posicao = i
print(maior)
print(posicao+1)