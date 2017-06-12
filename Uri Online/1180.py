# -*- coding: utf-8 -*-
N = int(input())
X = list(map(int, input().split()))
print("Menor valor: %d" % min(X))
for i in range(N):
    if X[i] == min(X):
        print("Posicao: %d" % i)