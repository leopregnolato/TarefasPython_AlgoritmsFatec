'''Escreva um programa que leia um número N (obrigatoriamente entre 0 e 50) e em seguida preencha uma lista
com N elementos inteiros gerados aleatoriamente entre 0 e 1000 (usar a função randint da biblioteca random –
veja o quadro sobre isso no exercício 9).
'''
from random import randint

N = int(input("Digite um valor de 0 a 50: "))
count = 0
A = []
i = 0

while N <= 0 and N >=50:
    print("Você digitou um número fora do intervalo permitido.") 
    N = int(input("Digite um valor de 0 a 50: "))

while count < N:
    B = randint(0, 1000)
    A.append(B)
    count = count + 1
    
print("\n\nA lista gerada foi:\n")
while i < N:
    print(A[i])
    i = i + 1

print("\n\nFim do programa")








