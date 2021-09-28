'''Escreva um programa que leia do teclado uma lista com tamanho de 10 elementos e exiba-o na tela na ordem
inversa à ordem de leitura, sendo um elemento por linha da tela.
'''

L = []
count = 0
i = 0

while count < 10:
    N = int(input("Digite um valor: "))
    if N <= 0:
        print("Digite um valor maior que 0")
    else:
        L.insert(0, N)
        count = count + 1

print("\n\nA lista gerada foi:\n")

while i < 10:
    print(L[i])
    i = i + 1

print("\n\nFim do programa")