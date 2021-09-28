'''
Escreva um programa que leia do teclado uma lista com tamanho de 10 elementos e exiba-o na tela um elemento
por linha.
'''

L = []
count = 0
i = 0

while count < 10:
    N = int(input("Digite o elemento {} da lista: ".format(count)))
    L.append(N)
    count = count + 1

print("\n\nA lista gerada foi:\n")

while i < 10:
    print(L[i])
    i = i + 1

print("\n\nFim do programa")