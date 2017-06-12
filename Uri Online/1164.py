# -*- coding: utf-8 -*-
X = int(input())
for x in range(X):
    N = int(input())
    soma = 0
    for i in range (1, N):
        if N % i == 0:
            soma += i
    if soma == N:
        print("%d eh perfeito" % N)
    else:
        print("%d nao eh perfeito" % N)