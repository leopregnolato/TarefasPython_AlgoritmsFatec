'''
Escreva um programa que leia um número inteiro N e preencha uma lista com N elementos inteiros digitados pelo
usuário. Exiba na tela a lista preenchida. Em seguida, o programa deve procurar e eliminar os elementos que
eventualmente estiverem repetidos deixando apenas a primeira ocorrência de cada valor. Apresentar a lista
resultante na tela.
'''

from random import randint

N = int(input("Digite N: "))

L = []
i = 0
while i < N:
    X = randint(0, 1000)
    L.append(X)
    i = i + 1

# Dados viciados para efeitos de teste. Devem ser retirados após a certeza de que a eliminação funciona    
N = 20
L = [989, 761, 52, 52, 52, 761, 91, 73, 945, 799, 915, 531, 799, 52, 612, 252, 303, 264, 580, 171]

print("\nLista L contém {} elementos:".format(len(L)))
print(L)

print("\nProcurando e eliminando valores repetidos em L")
print("\nA Lista original tem {} elementos".format(N))

contEliminados = 0
ref = 0
while ref < N - 1:
    i = N - 1
    while i > ref:
        if L[ref] == L[i]:
            contEliminados += 1
            del(L[i])
            N = N - 1
        i = i - 1
    ref += 1

if contEliminados > 0:
    print("  foram eliminados {} elementos".format(contEliminados))
else:
    print("  não houve eliminação de elementos")

print("\nLista resultante após a eliminação de repetidos tem {} elementos".format(N))
print(L)


print("\n\nFim do Programa")




