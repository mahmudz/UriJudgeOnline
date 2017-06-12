# -*- coding: utf-8 -*-
X = list([0]*10)
for i in range(10):
    X[i] = int(input())
for i in range(10):
    if X[i] <= 0:
        X[i] = 1
    print("X[%d] = %d" % (i, X[i]))