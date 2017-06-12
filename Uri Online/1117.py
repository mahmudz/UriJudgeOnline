# -*- coding: utf-8 -*-
aux = 0
cont = 0
while cont != 2:
    X = float(input())
    if X >= 0 and X <= 10:
        aux += X
        cont += 1
    else:
        print("nota invalida")
print("media = %.2f" % (aux / 2))