# -*- coding: utf-8 -*-
combustivel = [0, 0, 0]
while True:
    N = int(input())
    if N == 1:
        combustivel[0] += 1
    elif N == 2:
        combustivel[1] += 1
    elif N == 3:
        combustivel[2] += 1
    elif N == 4:
        break
print("MUITO OBRIGADO")
print("Alcool: %d" % combustivel[0])
print("Gasolina: %d" % combustivel[1])
print("Diesel: %d" % combustivel[2])