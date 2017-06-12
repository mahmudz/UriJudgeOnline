# -*- coding: utf-8 -*-
N = int(input())
for i in range(N):
    Num = int(input())
    if Num == 0: print("NULL")
    elif Num > 0 and Num % 2 == 0: print("EVEN POSITIVE")
    elif Num > 0 and Num % 2 != 0: print("ODD POSITIVE")
    elif Num < 0 and Num % 2 != 0: print("ODD NEGATIVE")
    else: print("EVEN NEGATIVE")