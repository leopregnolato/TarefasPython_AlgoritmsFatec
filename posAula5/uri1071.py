'''
Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números impares entre eles.

Entrada
O arquivo de entrada contém dois valores inteiros.

Saída
O programa deve imprimir um valor inteiro. Este valor é a soma dos valores ímpares que estão entre os valores fornecidos na entrada que deverá caber em um inteiro.
'''

X = int(input())
Y = int(input())
oddsum = 0
A = 0
B = 0
C = 0

if X < Y:
    A = X
    B = Y

else:
    B = X
    A = Y

if B % 2 == 0:
    C = B - 1
else:
    C = B - 2

if A == 0:
    print(0)

else:
    while A < C:
        if A % 2 != 0:
            A = A + 2
            oddsum = oddsum + A
        else:
            A = A + 1
            oddsum = oddsum + A
    
print(oddsum)       