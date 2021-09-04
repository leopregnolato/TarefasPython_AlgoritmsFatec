'''
Faça um programa que leia 6 valores. Estes valores serão somente negativos ou positivos (desconsidere os valores nulos). A seguir, mostre a quantidade de valores positivos digitados.

Entrada
Seis valores, negativos e/ou positivos.

Saída
Imprima uma mensagem dizendo quantos valores positivos foram lidos.
'''

count = 0
number = 0
positives = 0


while count < 6:    
    number = float(input())
    if number > 0:
        positives = positives + 1
    else:
        positives = positives
    count = count + 1


print("{} valores positivos".format(positives))
