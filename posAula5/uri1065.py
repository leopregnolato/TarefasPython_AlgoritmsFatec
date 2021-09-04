'''
Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.

Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída
Imprima a mensagem conforme o exemplo fornecido, indicando a quantidade de valores pares lidos.
'''

count = 0
number = 0
even = 0

while count < 5:    
    number = int(input())
    if number % 2 == 0:
        even = even + 1
    else:
        even = even
    count = count + 1

print("{} valores pares".format(even))