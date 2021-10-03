'''Refaça o exercício anterior generalizando-o para N valores inteiros digitados no teclado, onde N é um número
fornecido pelo usuário. Esse N deve ser usado no programa ao invés do tamanho fixo de 10 sugerido no programa
anterior. Colocar este programa no site do professor.'''

M = int(input("Digite o tamanho da lista: "))
LMin = int(input("Digite um valor mínimo: "))
LMax = int(input("Digite um valor máximo: "))

if LMax < LMin:
    X = LMax
    LMax = LMin
    LMin = X

A = []
count = 0

while count < M:
    N = int(input("Digite o {}° valor: ".format(count + 1)))
    if N >= LMin and N <=LMax:
        A.append(N)
        count = count + 1
    else:
        print("Valor {} fora do intervalo {} - {}!".format(N, LMin, LMax))


print("\nResultados:")
print("-----------------------------------------------------------------------------------------")
print("     Lista informada: {}".format(A))
print("     Quantidade de valores: {}".format(M))
print("-----------------------------------------------------------------------------------------")
print("\n\nFim do programa")