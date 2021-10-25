'''
Escreva um programa que preencha com números inteiros duas listas denominadas A e B com diferentes
tamanhos nA e nB, respectivamente. Em seguida o programa deve juntar as duas listas em uma única lista com o
tamanho nA+nB. Exibir na tela a lista resultante.
'''

from random import randint

nA = int(input("Digite nA: "))
A = []
for i in range(nA):
    A.append(randint(1, 50))

nB = int(input("Digite nA: "))
B = []
for i in range(nB):
    B.append(randint(1, 50))

nR = nA + nB
R = []
i = 0

while i < nA:
    R.append(A[i])
    i += 1

i = 0
while i < nB:
    R.append(B[i])
    i += 1

print("\nA Lista A tem {} elementos:".format(nA))
print(A)
print("\nA Lista B tem {} elementos:".format(nB))
print(B)
print("\nA Lista Resultante tem {} elementos:".format(nR))
print(R)

print("\n\nFim do Programa")