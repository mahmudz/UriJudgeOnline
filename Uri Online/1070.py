# -*- coding: utf-8 -*-
X = int(input())
aux = 0
i = X
while aux != 6:
    if i % 2 != 0:
        print(i)
        aux += 1
    i += 1