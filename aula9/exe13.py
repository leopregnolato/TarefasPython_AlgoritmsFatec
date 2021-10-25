'''Escreva um programa que leia um número inteiro N. Em seguida calcule e armazene em uma lista os N primeiros
números primos. Exibir a lista no final.
'''

N = int(input("Digite o tamanho da lista: "))
L = []

candidatoPrimo = 2 #primeiro primo
i = 0 #índice da lista

while i < N:
    cont = 0
    j = 2 #será o possível divisor do candidatoPrimo, se dividir, candidatoPrimo não é primo (Resto == 0)
    while j < candidatoPrimo: #na primeira rodada não entra aqui para que 2 seja adicionado a lista
        Resto = candidatoPrimo % j
        if Resto == 0:
            cont += 1 # mudar o valor de cont fará com que o candidatoPrimo não seja adicionado na lista
        j += 1 #verifica o próximo valor < que candidatoPrimo como próximo possível divisor
    if cont == 0:
        L.append(candidatoPrimo)
        i += 1
    candidatoPrimo += 1

print("\nLista com {} números primos:".format(N))
print(L)

print("\n\nFim do programa.")
    
