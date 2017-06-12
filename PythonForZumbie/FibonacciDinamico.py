# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
'''
Fibonacci
Fib(n) 1 2 3 4 5 6  7  8  9
   =   1 1 2 3 5 8 13 21 34
'''
def Fib(n):
    F1 = 1
    F2 = 1
    if n == 1 or n == 2:
        return 1
    else:
        for i in range(3, n+1):
            F = F1 + F2
            F2 = F1
            F1 = F
    return  F

X = int(input())
if Fib(X) % 2 == 0:
    print("Par")
else:
    print("Impar")
