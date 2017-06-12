# -*- coding: utf-8 -*-
L_Notas = [100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]
L_Troco = list([0]*12)
N = input()
N = float(N)
for i in range(len(L_Notas)):
    if N >= L_Notas[i]:
        L_Troco[i] = int(N / L_Notas[i])
        N -= L_Troco[i] * L_Notas[i]

print("NOTAS:")
for i in range (6):
    print("%d nota(s) de R$ %.2f" % (L_Troco[i], float(L_Notas[i])))
print("MOEDAS:")
for i in range (6,12):
    print("%d moeda(s) de R$ %.2f" % (L_Troco[i], float(L_Notas[i])))
