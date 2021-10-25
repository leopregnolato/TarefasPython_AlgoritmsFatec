'''
Escreva um programa que contenha um laço que será executado enquanto o número digitado for
diferente de zero. Para cada número digitado pelo usuário mostrar na tela apenas os que forem divisíveis
por 2 e por 3.
'''

N = 1

while N != 0:
    N = float(input("Digite um número: "))
    if (N % 2) == 0 and (N % 3) == 0:
        print(N)
    else:
        N = 1

print("\n\nFim do programa.")

