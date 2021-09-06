'''
Reescreva o programa anterior lendo um número inteiro adicional chamado Prim. Nesta versão o
programa deverá apresentar os N termos da sequência de Fibonacci que forem maiores que Prim.
'''

N = int(input("Digite um Número: "))
Prim = int(input("Digite outro número: "))
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