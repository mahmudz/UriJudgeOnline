# -*- coding: utf-8 -*-
import math
numeros = input()
numeros = numeros.split()
Delta = (float(numeros[1])**2) - (4 * float(numeros[0]) * float(numeros[2]))
if float(numeros[0]) != 0 and Delta >= 0:
    X1 = (-float(numeros[1]) + math.sqrt(Delta))/(2*float(numeros[0]))
    X2 = (-float(numeros[1]) - math.sqrt(Delta))/(2*float(numeros[0]))
    print("R1 = %.5f" % X1)
    print("R2 = %.5f" % X2)
else:
    print("Impossivel calcular")