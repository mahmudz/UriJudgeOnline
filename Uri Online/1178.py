# -*- coding: utf-8 -*-
N = float(input())
vetor = [N]
for i in range(1,100):
    vetor.append(vetor[-1]/2)
for i in range(100):
    print("N[%d] = %.4f" %(i, vetor[i]))