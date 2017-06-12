# -*- coding: utf-8 -*-
N = int(input())
vetor = list([0]*10)
for i in range(10):
    vetor[i] = N
    N = N * 2
    print("N[%d] = %d" % (i, vetor[i]))