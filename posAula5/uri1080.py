'''
Leia 100 valores inteiros. Apresente então o maior valor lido e a posição dentre os 100 valores lidos.

Entrada
O arquivo de entrada contém 100 números inteiros, positivos e distintos.

Saída
Apresente o maior valor lido e a posição de entrada, conforme exemplo abaixo.
'''

numbers = []
orderednumbers = []
major = 0
count = 0
maxindex = 0

while count < 100:
    numbers.append(int(input()))
    count = count + 1

orderednumbers = sorted(numbers)
major = orderednumbers[99]
maxindex = (numbers.index(major) + 1) 

print(major)
print(maxindex)