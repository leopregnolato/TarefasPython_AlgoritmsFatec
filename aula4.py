# #Primeira discussão: condicionais

# print("Primeiro programa com o comando if")
# A = int(input("Digite um valor para A: "))
# B = int(input("Digite um valor para B: "))

# if B != 0:
#     R = A / B
#     print("Divisão = ", R)
# else:
#     print("Não é possível dividir porque B = 0")

# print("\n\nFim do programa") 

'''Notar que esse programa tem as condições escritas de modo
diferente do pdf da aula, para enfatizar que um mesmo problema
pode ser resolvido com diferentes códigos'''

# #Segunda discussão: tipos de condições

# #sobre a ordem dos caracteres na tabela ASCII
# print(ord("A"))
# print(ord("I"))
# print(ord("Í"))
# print(ord("i"))

# print( "A" > "a")
# print( "a" > "A")

# #Sobre o trablaho com números reais e suas peculiaridades

# X = 3.000000000001
# Y = 3.000

# print("X = {:.3f}".format(X))
# print("Y = {:.3f}".format(Y))

# print(X == Y)

# print(abs(X-Y) < 0.0009) #essa é a maneira de considerar se X == Y





'''
***ANOTAÇÕES DE AULA***

> Na comunidade Python o padão de identação são 4 espaços;

> Literal (o valor em si) ou variáveis: as condicionais podem
ser feitas com ambos;

> Em comparação de strings é comparado na ordem alfabética. Os 
critérios seguintes seguem a ordem da tabela ASCII, que é a 
tabela que padroniza os binários que correspondem aos caracteres;

> O Unicode é a ampliação do ASCII para contemplar
os caracteres dos outros idiomas (com referência ao inglês, a língua
na qual os computadores foram deses)

> Em condicionais a tabela ASCII é a referência para a ordenação dos 
caracteres;

> A função abs() traz o módulo ou magnitude de um número, e esse módulo é
útil para comparação de valores reais;

> Tomar cuidado EXTREMO com condicionais ou comparações entre valores reais uma vez que 
a precisão desse conjunto numérico é difícil de determinar.

> Em testes lógico é importante notar a ordem de precedência dos operadores NOT, AND
e OR: NOT em primeiro, AND em seguida e OR por último;

> comando print com format()
    print("X = {}".format(X))
    print("X = {:.3f}".format(X)) #controlar o número de casas decimais

'''