'''
Elaborar um programa que apresente o somatório dos valores pares existentes na faixa entre 1 e N,
onde N é um número digitado pelo usuário e que deve ser no mínimo 100 (obrigatório garantir esse
requisito).
'''

N = int(input("Digite um número maior ou igual a 100: "))
count = 0
sum = 0
total = 0

if N >= 100:
    while count < N:
        sum = sum + 2
        total = total + sum
        count = count + 2
    print("Somatório: {}".format(total))
else:
    print("Número inválido")


