'''
Escreva um programa que leia do teclado duas listas com tamanho 10, com números inteiros. Em seguida o
programa deve juntar as duas listas em uma única lista com o tamanho 20.
'''

L1 = []
L2 = []
count = 0 

print("\nCriando a 1ª lista: ")

while count < 10:
    N = int(input("     Digite o {}º valor da lista 1: ".format(count + 1)))
    L1.append(N)
    count += 1

print("\nCriando a 2ª lista: ")

count = 0 

while count < 10:
    N = int(input("     Digite o {}º valor da lista 2: ".format(count + 1)))
    L1.append(N)
    count += 1

print("\n\nJuntando as duas listas...")

L = L1 + L2

print("\n\nA lista final é:")
print(L)

print("\n\nFim do programa.")


