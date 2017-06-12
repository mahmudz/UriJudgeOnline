# -*- coding: utf-8 -*-
qtd_gritos = 0
soma_pontos = [0, 0, 0]
while qtd_gritos != 3:
    entrada = str(input())
    if entrada[0] != "c":
        entrada = list(entrada)
        if entrada[0] == '*':
            soma_pontos[qtd_gritos] += 4
        if entrada[1] == '*':
            soma_pontos[qtd_gritos] += 2
        if entrada[2] == '*':
            soma_pontos[qtd_gritos] += 1
    else:
        qtd_gritos += 1
print(soma_pontos[0])
print(soma_pontos[1])
print(soma_pontos[2])