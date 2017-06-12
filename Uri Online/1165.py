# -*- coding: utf-8 -*-
N = int(input())
for i in range(N):
    X = int(input())
    cont = 0
    for teste in range(1, X+1):
        if X % teste == 0:
            cont += 1
    if cont == 2:
        print("%d eh primo" % X)
    else:
        print("%d nao eh primo" % X)