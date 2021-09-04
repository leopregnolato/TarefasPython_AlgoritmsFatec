'''
Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares, quantos valores digitados foram ímpares, quantos valores digitados foram positivos e quantos valores digitados foram negativos.

Entrada
O arquivo de entrada contém 5 valores inteiros quaisquer.

Saída
Imprima a mensagem conforme o exemplo fornecido, uma mensagem por linha, não esquecendo o final de linha após cada uma.
'''

count = 0
number = 0
even = 0
odd = 0
positive = 0
negative = 0

while count < 5:    
    number = int(input())
    if number % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
    if number > 0:
        positive = positive + 1
    elif number < 0:
        negative = negative +1
    count = count + 1

print("{} valor(es) par(es)".format(even))
print("{} valor(es) impar(es)".format(odd))
print("{} valor(es) positivo(s)".format(positive))
print("{} valor(es) negativo(s)".format(negative))