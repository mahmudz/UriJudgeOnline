# -*- coding: utf-8 -*-
while True:
    N = int(input())
    if N != 0:
        aux = 0
        soma = 0
        while aux != 5:
            if N % 2 == 0:
                soma += N
                aux += 1
            N += 1
        print(soma)
    else:
        break