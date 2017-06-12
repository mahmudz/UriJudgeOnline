# -*- coding: utf-8 -*-
salario = float(input())
n_salario = 0

if salario <= 400:
    n_salario = salario + (salario * 0.15)
    print("Novo salario: %.2f" %n_salario)
    print("Reajuste ganho: %.2f" % (n_salario - salario))
    print("Em percentual: 15 %")
elif salario > 400 and salario <= 800:
    n_salario = salario + (salario * 0.12)
    print("Novo salario: %.2f" % n_salario)
    print("Reajuste ganho: %.2f" % (n_salario - salario))
    print("Em percentual: 12 %")
elif salario > 800 and salario <= 1200:
    n_salario = salario + (salario * 0.1)
    print("Novo salario: %.2f" % n_salario)
    print("Reajuste ganho: %.2f" % (n_salario - salario))
    print("Em percentual: 10 %")
elif salario > 1200 and salario <= 2000:
    n_salario = salario + (salario * 0.07)
    print("Novo salario: %.2f" % n_salario)
    print("Reajuste ganho: %.2f" % (n_salario - salario))
    print("Em percentual: 7 %")
else:
    n_salario = salario + (salario * 0.04)
    print("Novo salario: %.2f" % n_salario)
    print("Reajuste ganho: %.2f" %(n_salario - salario))
    print("Em percentual: 4 %")