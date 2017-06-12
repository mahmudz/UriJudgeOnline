# -*- coding: utf-8 -*-
soma_positivos = 0
qtd_positivos = 0
for i in range(6):
    N = float(input())
    if N > 0:
        qtd_positivos += 1
        soma_positivos += N
print("%d valores positivos" %qtd_positivos)
resultado = float(soma_positivos)/float(qtd_positivos)
print("%.1f" %resultado)

