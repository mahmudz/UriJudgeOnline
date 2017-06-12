# -*- coding: utf-8 -*-
N = int(input())
Horas = 0
if N < (24*60):
    Min = int(N / 60)
    Seg = N % 60
else:
    Horas = int(N / 3600)
    Aux = N - (Horas * 3600)
    Min = (Aux / 60)
    Seg = Aux % 60
print("%d:%d:%d" % (Horas, Min, Seg))