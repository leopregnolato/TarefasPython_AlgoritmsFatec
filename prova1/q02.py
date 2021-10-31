print("Daniel Marcionilo Pedroso do Rosario Silva, RA: 21206301")
print("Leonardo Antonio Pregnolato, RA: 21206393")
print("Questão 2\n\n")

'''
Escreva um programa que leia dois números inteiros LMin e LMax que serão os limites de uma faixa de valores. É obrigatório que
LMin seja maior que zero e que LMax seja maior que LMin. O programa também deve ler um terceiro número inteiro X
obrigatoriamente diferente de zero. O programa deve garantir estes três requisitos.
Em seguida, o programa deve permanecer em laço lendo valores inteiros do teclado enquanto não for digitado zero. Todo valor lido
do teclado deve ser colocado em uma lista apenas se cumprir três requisitos:
a) estiver dentro da faixa definida por [LMin, LMax]
b) ser divisível por X
c) e não estar na lista (ou seja, não pode haver repetidos)
Ao final, o programa tem que mostrar na tela a lista completa, a quantidade de elementos da lista, a soma de todos os seus valores
e a média deles.
'''


LMin = int(input("Digite Mínimo: ")) 
LMax = int(input("\nDigite Máximo: "))


while (LMin <= 0 and LMax <= 0) or (LMin == LMax):
    print("Digite valores maiores que 0! E os valores não podem ser iguais!")
    LMin = int(input("Digite Mínimo: ")) 
    LMax = int(input("\nDigite Máximo: "))


if LMin > LMax:
    LMin, LMax = LMax, LMin 

X = int(input("\nDigite o valor de X: "))

while X == 0:
    print("Digite X > 0")
    X = int(input("Digite o valor de X: "))

L = []
TamL = 0
soma = 0
N = int(input("\nDigite o valor de N: "))

while N != 0: 
    if (N >= LMin and N <= LMax) and (N % X == 0):
        
        jaEsta = False
        j = 0 
        while j < TamL: 
            if L[j] == N:
                jaEsta = True
            j += 1
                    
        
        if jaEsta == False:
            L.append(N)
            TamL += 1
            soma += N
            N = int(input("\nDigite o valor de N: "))
                    
        else:
            print("     ...o valor {} já está na lista! Digite outro por favor.\n".format(N))
            N = int(input("\nDigite o valor de N: "))
    else:
        N = int(input("\nDigite o valor de N: "))

if TamL != 0: 
    print(L)
    print(TamL)
    print(soma)
    media = soma / TamL
    print(media)
    print("Fim do programa")
else:
    print("Não foi criada nenhuma lista!")
    print("Fim do programa")



