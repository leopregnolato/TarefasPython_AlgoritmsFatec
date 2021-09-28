'''Escreva um programa que leia um número N (obrigatoriamente entre 0 e 50) e em seguida leia N números reais
em uma lista A. Exiba a lista na tela, um elemento por linha.
'''

N = int(input("Digite um valor de 0 a 50: "))
count = 0
A = []
i = 0

while N <= 0 and N >=50:
    print("Você digitou um número fora do intervalo permitido.") 
    N = int(input("Digite um valor de 0 a 50: "))

while count < N:
    B = float(input("Digite um valor para a lista: "))
    A.append(B)
    count = count + 1
print("\n\nA lista gerada foi:\n")
while i < N:
    print(A[i])
    i = i + 1


    
print("\n\nFim do programa")