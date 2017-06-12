# -*- coding: utf-8 -*-
N = int(input())
fibonacci = list([0]*N)
fibonacci[0] = 0
fibonacci[1] = 1
fibonacci[2] = 1
for i in range(3, N):
    fibonacci[i] = fibonacci[i-1] + fibonacci[i-2]
for i in range(len(fibonacci)):
    if i != len(fibonacci)-1:
        print(fibonacci[i], end=" ")
    else:
        print(fibonacci[i])