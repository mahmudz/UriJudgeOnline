# -*- coding: utf-8 -*-
'''
Fibonacci
Fib(n) 1 2 3 4 5 6  7  8  9
   =   1 1 2 3 5 8 13 21 34
'''
def Fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return Fib(n-1) + Fib(n-2)


X = int(input())
if Fib(X) % 2 == 0:
    print("Par")
else:
    print("Impar")