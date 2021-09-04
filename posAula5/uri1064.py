'''
Leia 6 valores. Em seguida, mostre quantos destes valores digitados foram positivos. Na próxima linha, deve-se mostrar a média de todos os valores positivos digitados, com um dígito após o ponto decimal.

Entrada
A entrada contém 6 números que podem ser valores inteiros ou de ponto flutuante. Pelo menos um destes números será positivo.

Saída
O primeiro valor de saída é a quantidade de valores positivos. A próxima linha deve mostrar a média dos valores positivos digitados.
'''

count = 0
number = 0
positives = 0
mean = 0

while count < 6:    
    number = float(input())
    if number > 0:
        positives = positives + 1
        mean = mean + number
    else:
        positives = positives
    count = count + 1
mean = mean / positives

print("{} valores positivos".format(positives))
print("{:.1f}".format(mean))