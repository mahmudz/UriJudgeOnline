# -*- coding: utf-8 -*-
while True:
    X, Y = input().split()
    X, Y = int(X), int(Y)
    if X > 0 and Y > 0:
        if Y > X:
            Y, X = X, Y
        aux = 0
        for i in range(Y, X+1):
            aux += i
            print(i, end=" ")
        print("Sum=%d" % aux)
    else:
        break