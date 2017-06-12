# -*- coding: utf-8 -*-
N = int(input())
for i in range(N):
    Num = input()
    Num = Num.split()
    resultado = (((float(Num[0])*2) + (float(Num[1])*3) + (float(Num[2])*5))/10)
    print("%.1f" % resultado)
