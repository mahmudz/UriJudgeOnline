# -*- coding: utf-8 -*-
T = int(input())
fibonacci = [0, 1, 1]
for i in range(T):
    N = int(input())
    if N <= 2:
        print("Fib(%d) = %d" %(N, fibonacci[N]))
    elif N < len(fibonacci):
        print("Fib(%d) = %d" % (N, fibonacci[N]))
    else:
        for x in range(len(fibonacci)-1, N+1):
            fibonacci.append(fibonacci[-1]+fibonacci[-2])
        print("Fib(%d) = %d" % (N, fibonacci[N]))
        #print(fibonacci)