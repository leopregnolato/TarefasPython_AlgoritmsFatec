'''
Escreva um programa que leia do teclado dois números inteiros nA e nB e leia também duas listas denominados
A e B com os tamanhos nA e nB, respectivamente. Na leitura de cada uma das listas é obrigatório que não sejam
aceitos valores repetidos. Em seguida, o programa deve juntar as duas listas em um única lista R (resultante)
tomando o cuidado de que a lista R não deve ter valores duplicados.
'''

def estaNaLista(valor, Lista, Tam):
    j = 0
    while j < Tam:
        if Lista[j] == valor:
            return True
        j += 1
    return False


#criando a lista A:
nA = int(input("Digite o tamanho da lista A: "))
A = []
TamA = 0
i = 0

while i < nA:
    x = int(input("Digite o elemento {} da lista A: ".format(i)))
    if estaNaLista(x, A, TamA):
        print("...o valor {} já está na lista!\n".format(x))
    else:
        A.append(x)
        TamA += 1
        i += 1


#criando a lista B:
nB = int(input("Digite o tamanho da lista B: "))
B = []
TamB = 0
i = 0

while i < nB:
    x = int(input("Digite o elemento {} da lista B: ".format(i)))
    if estaNaLista(x, B, TamB):
        print("...o valor {} já está na lista!\n".format(x))
    else:
        B.append(x)
        TamB += 1
        i += 1

print("\nA Lista A tem {} elementos".format(TamA))
print(A)
    
print("\nA Lista B tem {} elementos".format(TamB))
print(B)

R = []
TamR = nA # TamR recebe o tamanho de A pois sabemos que em A não há elementos repetidos
i = 0
while i < nA:
    R.append(A[i])
    i += 1


i = 0
while i < nB:
    if not estaNaLista(B[i], R, len(R)):
        R.append(B[i])
        TamR += 1
    i += 1

print("\nA Lista R tem {} elementos".format(TamR))
print(R)

print("\n\nFim do Programa")

