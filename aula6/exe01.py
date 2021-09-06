'''
Escreva um programa que leia um número inteiro e em seguida apresente na tela a tabuada de 0 a 10
para esse número fornecido. Siga o formato apresentado abaixo (supondo que foi digitado 4):
4 x 1 = 4
4 x 2 = 8
4 x 3 = 12
...
4 x 10 = 40
'''
arquivo = open('exe01.txt', 'w+')
N = int(input())
count = 0
result = 0
mult = 0

while count < 10:
    mult = count + 1
    result = N * mult
    print("{} X {} = {}".format(N, mult, result), file=arquivo)
    count = count + 1

arquivo.close()
