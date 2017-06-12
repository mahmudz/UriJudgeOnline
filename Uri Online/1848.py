# -*- coding: utf-8 -*-
qtd_gritos = 0
soma_pontos = 0
while qtd_gritos != 3:
    entrada = str(input())
    if entrada[0] != "c":
        entrada = list(entrada)
        if entrada[0] == '*':
            soma_pontos += 4
        elif entrada[1] == '*':
            soma_pontos += 2
        elif entrada[2] == '*':
            soma_pontos += 1
    else:
        qtd_gritos += 1
        print(soma_pontos)
        soma_pontos = 0

