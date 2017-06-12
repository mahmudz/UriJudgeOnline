# -*- coding: utf-8 -*-
N = int(input())
texto = input().split()
for i in range (N):
    if texto[i][0] == 'O' and texto[i][1] == 'B' and len(texto[i]) == 3:
        texto[i] = "OBI"
    if texto[i][0] == 'U' and texto[i][1] == 'R' and len(texto[i]) == 3:
        texto[i] = "URI"
print(" ".join(texto))