# -*- coding: utf-8 -*-
#Matriz Quadratica
N = int(input("Digite a dimensao da matriz: "))
#Criando Linhas na Matriz1
matriz1 = [0] * N
#Criando Colunas na matriz1
for i in range(N):
    matriz1[i] = [0] * N
#Preenchendo diagonal
'''
for i in  range(N):
    matriz1[i][i] = 1
'''
for i in range(N):
    print(matriz1[i])
