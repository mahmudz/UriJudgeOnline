# -*- coding: utf-8 -*-
N1 = int(input())
N2 = int(input())
if N2 < N1:
    N1, N2 = N2, N1
soma = 0
for i in range (N1, N2 +1):
    if i % 13 != 0:
        soma += i
print(soma)