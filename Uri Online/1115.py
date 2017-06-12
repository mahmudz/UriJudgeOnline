# -*- coding: utf-8 -*-
C = [0, 0]
while True:
    C[0], C[1] = input().split()
    C[0] = int(C[0])
    C[1] = int(C[1])
    if C[0] != 0 and C[1] != 0:
        if C[0] > 0 and C[1] > 0:
            print("primeiro")
        elif C[0] < 0 and C[1] < 0:
            print("terceiro")
        elif C[0] < 0 and C[1] > 0:
            print("segundo")
        else:
            print("quarto")
    else:
        break