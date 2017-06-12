# -*- coding: utf-8 -*-
N = int(input())
result = list([0]*N)
for i in range(N):
    X, Y = input().split()
    X = int(X)
    Y = int(Y)
    if Y < X:
        X, Y = Y, X
    aux = 0
    for y in range(X+1, Y):
        if y % 2 != 0:
            aux += y
    result[i] = aux
for i in result:
    print(i)