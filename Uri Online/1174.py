# -*- coding: utf-8 -*-
entrada = list([0]*100)
for i in range(10):
    entrada[i] = float(input())

for i in range(10):
    if entrada[i] <= 10:
        print("A[%d] = %.1f" % (i, entrada[i]))