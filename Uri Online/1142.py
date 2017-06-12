# -*- coding: utf-8 -*-
N = int(input())
aux = 1
for i in range(1, (N*4)+1):
    if aux == 4:
        print("PUM")
        aux = 1
    else:
        print(i, end=' ')
        aux += 1