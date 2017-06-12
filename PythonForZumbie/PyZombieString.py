palavra = input()
aux = True
for i in range(len(palavra)):
    if palavra[i] != palavra[-i-1]:
        aux = False
if aux == True:
    print("Palavra Palindrome")
else:
    print("Palavra nao Palindrome")
'''
Outra maneira de resolver!

if palavra == palavra[::-1]:
    print("Palindrome")
else:
    print("Nao ´e palindrome")
'''
