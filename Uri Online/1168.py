# -*- coding: utf-8 -*-
valores = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6, 6]
leds = 0
N = int(input())
for i in range(N):
    numero = list(input())
    for i in range (10):
        leds += numero.count(str(i)) * valores[i]
    print("%d leds" %leds)
    leds = 0