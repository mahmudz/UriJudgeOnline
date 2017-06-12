# -*- coding: utf-8 -*-
moedas = [100, 50, 25, 5, 1]
moedas2 = [0]*len(moedas)

valor = int(input("Informe o valor: "))

aux = 0
qtd_moedas = 0
while valor != 0:
    if valor >= moedas[aux]:
        qtd_moedas += 1
        moedas2[aux] += 1
        valor -= moedas[aux]
    else:
        aux += 1
print("Menor qtd de moedas: %d" % qtd_moedas)
for i in range(len(moedas)):
    print("%d moedas de %d" %(moedas2[i], moedas[i]))