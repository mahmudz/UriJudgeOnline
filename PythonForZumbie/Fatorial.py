# -*- coding: utf-8 -*-
def Fatorial (x):
    soma = 1
    for i in range(1,x+1):
        soma *= i
    return soma


print(Fatorial(5))