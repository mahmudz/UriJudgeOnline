# -*- coding: utf-8 -*-
soma = 0
cont = 0
while True:
    N = float(input())
    if N < 0:
        break
    else:
        soma += N
        cont += 1
print("%.2f" % float(soma / cont))