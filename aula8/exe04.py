'''
Escreva um programa que leia do teclado duas listas com tamanho 10, com números inteiros. Em seguida
o programa deve juntar as duas listas em uma única com o tamanho 20.
'''

L = []
M = []
count = 0

while count < 10:
    N = int(input("Digite um número para a PRIMEIRA lista: "))
    L.append(N)
    count = count + 1

count = 0

while count < 10:
    N = int(input("Digite um número para a SEGUNDA lista: "))
    M.append(N)
    count = count + 1

print(L + M)
print("\n\nFim do Programa")