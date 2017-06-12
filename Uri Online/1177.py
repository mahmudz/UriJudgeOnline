# -*- coding: utf-8 -*-
N = int(input())
vetor = []
while len(vetor) < 1000:
    for i in range(N):
        if len(vetor) < 1000:
            vetor.append(i)
        else:
            break
for i in range(len(vetor)):
    print("N[%d] = %d" % (i, vetor[i]))