# -*- coding: utf-8 -*-
while True:
    X, Y = input().split()
    X, Y = int(X), int(Y)
    if X != Y:
        if X > Y:
            print("Decrescente")
        else:
            print("Crescente")
    else:
        break