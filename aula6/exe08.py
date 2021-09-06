'''
Desenvolva um programa que leia do teclado um número inteiro e mostre na tela se esse número é
primo ou não. Lembrando: um número primo é divisível somente por 1 e por ele mesmo.
'''

N = int(input("Digite um número: "))

if (N % 2 == 0) or (N % 3 == 0) or (N % 7 == 0) or (N % 11 == 0):
    print("Não é um número primo!")
else:
    print("É um número primo!")