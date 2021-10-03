'''Escreva um programa que leia um número inteiro N e preencha uma lista com N elementos inteiros gerados
aleatoriamente entre 0 e 1000 (usar a função randint da biblioteca random). Exiba na tela a lista gerada. Em
seguida, o programa deve ler um valor X e informar se tal valor está, ou não está presente na lista. Neste exercício
é permitido usar os operadores in e/ou not in. '''

from random import randint

N = int(input("Digite o tamanho da lista: "))

A = []
count = 0

while count < N:
    B = randint(0, 1000)
    A.append(B)
    count = count + 1

print("-----------------------------------------------------------------------------------------")
print("Lista gerada: {}".format(A))
print("-----------------------------------------------------------------------------------------")

X = int(input("Digite um valor: "))

if X in A:
    print("O valor {} está na lista!".format(X))
else:
    print("     O valor {} não está na lista!".format(X))
print("-----------------------------------------------------------------------------------------")
print("\n\nFim do programa")
