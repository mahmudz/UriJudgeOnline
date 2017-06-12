# -*- coding: utf-8 -*-
N = int(input())
Num = [0, 0]
for i in range(N):
    Num[0], Num[1] = input().split()
    Num[0] = float(Num[0])
    Num[1] = float(Num[1])
    try:
        aux = Num[0] / Num[1]
        print("%.1f" %aux)
    except:
        print("divisao impossivel")