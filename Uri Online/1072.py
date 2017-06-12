# -*- coding: utf-8 -*-
N = int(input())
aux = 0
for i in range(N):
    X = int(input())
    if X >= 10 and X < 20:
        aux +=1
print(aux,"in")
print(N-aux,"out")