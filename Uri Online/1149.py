# -*- coding: utf-8 -*-
soma = 0
A = input().split()
A[0], A[1] = int(A[0]), int(A[1])
while A[1] <= 0:
    A[1] = input()
    A[1] = int(A[1])
for i in range(A[1]):
    soma += A[0]
    A[0] +=1
print(soma)