'''Refaça o exercício anterior de modo que os valores inválidos, ou seja, os que estão fora do intervalo [Min, Max]
sejam inseridos em uma segunda lista chamada R. Apresentar na tela a lista de valores aceitos (lista A) e a lista de
valores rejeitados (lista R), bem como o tamanho de cada um. Colocar este programa no site do professor.'''

M = int(input("Digite o tamanho da lista: "))
LMin = int(input("Digite um valor mínimo: "))
LMax = int(input("Digite um valor máximo: "))

if LMax < LMin:
    X = LMax
    LMax = LMin
    LMin = X

A = []
R = []
count = 0

while count < M:
    N = int(input("Digite o {}° valor: ".format(count + 1)))
    if N >= LMin and N <=LMax:
        A.append(N)
        count = count + 1
    else:
        print("O valor {} foi rejeitado!".format(N))
        R.append(N)

Rlenght = len(R)

print("\nResultados:")
print("-----------------------------------------------------------------------------------------")
print("LISTA ACEITA:")
print("     Lista informada: {}".format(A))
print("     Quantidade de valores: {}".format(M))
print("-----------------------------------------------------------------------------------------")
print("LISTA DE VALORES REJEITADOS:")
print("     Lista informada: {}".format(R))
print("     Quantidade de valores: {}".format(Rlenght))
print("-----------------------------------------------------------------------------------------")
print("\n\nFim do programa")