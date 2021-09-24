'''
Escreva um programa que permaneça em laço até que seja digitado o valor zero ou negativo. Cada valor
positivo lido deve ser inserido no final de uma lista, usando o método append. Ao final exiba a lista
completa na tela.
'''

N = float(input("Digite um número: "))
L = []

while N > 0:
    L.append(N)
    N = float(input("Digite um número: "))

print(L)

print("\n\nFim do programa")