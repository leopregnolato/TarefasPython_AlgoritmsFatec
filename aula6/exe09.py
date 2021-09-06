'''
Escreva um programa que leia um número inteiro N e em seguida apresente na tela os N primeiros
termos da sequência de Fibonacci. Essa sequência tem como regra de formação o fato de um número
ser a soma dos dois anteriores, sendo que os dois primeiros termos da sequência são, respectivamente,
0 e 1.
Caso de Teste: se N = 9 então a sequência é: 0, 1, 1, 2, 3, 5, 8, 13, 21
'''

N = int(input("Digite um Número: "))
count = 0
A = 0 
B = 1
print(A)
print(B)

while count < (N - 2):
    elemA = A
    elemB = B
    elemC = elemA + elemB
    print(elemC)
    A = elemB
    B = elemC
    count = count + 1

