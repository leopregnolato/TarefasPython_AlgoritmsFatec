'''
Escreva um programa que leia do teclado uma lista com tamanho de 10 elementos e exiba-a na tela na
ordem inversa à ordem de leitura.
'''

L = []
count = 0

while count < 10:
    N = float(input("Digite um número: "))
    L.insert(0, N)
    count = count + 1

print(L)
print("\n\nFim do programa")

