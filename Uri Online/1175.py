# -*- coding: utf-8 -*-
vetor = list([0]*20)
for i in range(20):
    vetor[i] = int(input())
for i in range(10):
    vetor[i], vetor[-i-1] = vetor[-i-1], vetor[i]
for i in range(20):
    print("N[%d] = %d" % (i, vetor[i]))