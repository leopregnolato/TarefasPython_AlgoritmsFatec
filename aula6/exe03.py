'''
Escreva um programa que leia um número inteiro N e em seguida leia N números reais, separando o
menor e o maior, apresentando-os na tela.
'''

N = int(input("Digite um número: "))
count = 0
numbers = []
minor = 0
major = 0


while count < N:
        numbers.append(float(input("Digite o {}º número real: ".format(count +1))))
        count = count + 1

orderednumbers = sorted(numbers)

minor = orderednumbers[0]
major = orderednumbers[N - 1]

print("O menor número é {}".format(minor))
print("O maior número é {}".format(major))

