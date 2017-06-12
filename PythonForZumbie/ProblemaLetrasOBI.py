# -*- coding: utf-8 -*-
letra = str(input())
texto = input().split()

cont = 0

for i in range(len(texto)):
    if letra in texto[i]:
        cont += 1
resultado = (float(cont)*100.0) / len(texto)
print("Porcentagem: %.1f" %resultado)