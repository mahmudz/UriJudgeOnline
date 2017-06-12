# -*- coding: utf-8 -*-
X = int(input())
Y = int(input())
if Y < X:
    X, Y = Y, X
for i in range(X+1, Y):
    if int(i % 5) == 2 or int(i % 5) == 3:
        print(i)