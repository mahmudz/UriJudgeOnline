# -*- coding: utf-8 -*-
par = 0
impar = 0
positivo = 0
negativo = 0
for i in range (5):
    X = int(input())
    if X > 0:
        positivo += 1
    elif X < 0:
        negativo +=1
    if X % 2 == 0:
        par += 1
    else:
        impar += 1

print("%d valor(es) par(es)" % par)
print("%d valor(es) impar(es)" % impar)
print("%d valor(es) positivo(s)" % positivo)
print("%d valor(es) negativo(s)" % negativo)