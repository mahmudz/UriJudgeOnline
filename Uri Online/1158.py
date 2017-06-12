# -*- coding: utf-8 -*-
N = int(input())
resultados = list([0]*N)
for i in range(N):
    X, Y = input().split()
    X = int(X)
    Y = int(Y)
    cont = 0
    soma = 0
    while True:
        if cont != Y:
            if X % 2 != 0:
                soma += X
                cont += 1
            X += 1
        else:
            break
    resultados[i] = soma
for i in resultados:
    print(i)