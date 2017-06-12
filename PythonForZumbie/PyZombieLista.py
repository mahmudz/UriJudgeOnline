letras = []
for i in range (10):
    letras.append(input())

vogais = "aeiou"
n_vogais = 0
n_consoantes = 0
for i in range (10):
    if letras[i] in vogais:
        n_vogais += 1
    #if letras[i] not in vogais:
    else:
        n_consoantes += 1

print(letras)
print("Numero de vogais: ", n_vogais)
print("Numero de consoantes: ", n_consoantes)
