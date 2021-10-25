'''Escreva um programa que leia um número inteiro N e preencha uma lista com N elementos inteiros gerados
aleatoriamente entre 0 e 1000. Exiba na tela a lista gerada. Em seguida, o programa deve ler um valor X e, caso X
esteja na lista, deve eliminá-lo. Caso haja várias ocorrências de X, todas devem ser eliminadas. Pesquise como
usar a função del (você vai precisar dela e neste exercício será permitido usá-la).'''

from random import randint

N = int(input("Digite o tamanho da lista: "))

A = []
count = 0

while count < N:
    B = randint(0, 10)
    A.append(B) 
    count = count + 1   

# Dados viciados para efeitos de teste. Devem ser retirados após a certeza de que a eliminação funciona    
N = 20
A = [989, 761, 52, 52, 52, 761, 91, 73, 945, 799, 915, 531, 799, 52, 612, 252, 303, 264, 580, 171]

print("\nAlista contém {} elementos:".format(len(A)))
print(A)

X = int(input("\n\nDigite X: "))
print("\nProcurando {} e eliminando da lista...".format(X))

#busca sequencial ou busca linear
contEliminados = 0
i = 0

while i < N:
    if A[i] == X:
        contEliminados += 1
        print("     encontrado na posição {} - ELIMINADO".format(i))
        del(A[i])
        N = N - 1 
    else:
        i += 1

if contEliminados > 0:
    print("     Foram eliminados {} elementos".format(contEliminados))
    print("\n\nLista após a eliminação de {}".format(X))
    print(A)
else:
    print("     Não houve eliminados já que {} não está na lista.".format(X))

print("\n\nFim do programa")