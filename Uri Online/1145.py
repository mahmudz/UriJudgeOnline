# -*- coding: utf-8 -*-
X, Y = input().split()
X, Y = int(X), int(Y)
aux = 1
for i in range(1, Y+1):
    if aux < X and i != Y+1:
        print(i, end=" ")
        aux += 1
    else:
        print(i)
        aux = 1