##### Estudo da Aula 3

# Base = 10.3
# Altura = 4
# Area = Base * Altura
# print(Area)
# print(type(Base))
# print(type(Altura))
# print(type(Area))

# x = 1.0
# print(type(x))
# y = 18
# print(type(y))
# z = x + y
# print(type(z))
# a = 5 + 3j
# print(type(a))
# print(type(A))
#
# A = 14
# B = 5
# C= A ** B
# print(C)

##### Exercício 1
# X = 0.0
# print("Tipo da variável X:", type(X))
# Y = 18
# print("Tipo da variável Y:", type(Y))
# Z = X + Y
# print("Tipo da variável Z:", type(Z))

##### Exercício 2
#
# a = 20
#
# print(type(A))
#
# Variável A não definida
#
# Traceback (most recent call last):
#   File "/home/leopregnolato/Workspace/TarefasPython_AlgoritmsFatec/Aula03.py", line 38, in <module>
#     print(type(A))
# NameError: name 'A' is not defined

##### Exercício 3

# S = "FATEC SÃO PAULO"
# print("Tipo da variável S:", type(S))
# #Tipo da variável S: <class 'str'>

##### Exercício 5

Base = 9
Altura = 6
Area = (Base * Altura) / 2
print("A área de um triângulo de base", Base , "e altura", Altura , "é igual a", Area)
#A área de um triângulo de base 9 e altura 6 é igual a 27.0

##### Exercício 6

horaTrabalho = 14.25
horaExtra = horaTrabalho * 2
cargaTrabalho = 163
cargaExtra = 20
salarioBruto = (horaTrabalho * cargaTrabalho) + (horaExtra * cargaExtra)
print("O salário bruto de um trabalhador que trabalhou", cargaTrabalho, "horas e mais", cargaExtra, "horas extras, receberá um salário bruto de R$", salarioBruto)
#O salário bruto de um trabalhador que trabalhou 163 horas e mais 20 horas extras, receberá um salário bruto de R$ 2892.75

##### Exercício 7

A = 4
B = 5
C = 1

R = (A + B) / 2
print(R)
# 2.4444444444444446

R = ( (3 * A) + (2 * B) ) / (A + B)
print(R)

x = (- B + ( ( (B ** 2) - (4 * A * C) ) ** 0.5)) / (2 * A)
print(x)
# -0.25

Z = (7.6 * A) - (B ** 1.7)
print(Z)
# 14.974153431999758

##### Exercício 8

# O comando input() serve para que o Python capture o que o usuário digitar.
#Isso permite que os dados fornecidos sejam atribuídos a uma variável. No entanto, mesmo
# que o usuário digite um numero, a informação é salva como uma string. Caso seja necessário a conversão do tipo da variável pode ser feita. Os exemplos
# a seguir ilustram como podemos usar esse comando.
#Exemplo A: uso simplificado do comando, dando a instrução ao usuário como parâmetro da função:
nome = input("Digite o seu nome:")
print(nome)
print(type(nome))

#Saída:
# Digite o seu nome:Leo
# Leo
# <class 'str'>

#Exemplo B: Outro modo de empregar o comando sem o parâmetro da função. As saídas mostram que todos os dados recolhidos são salvos como string.
print("Digite o seu nome:")
nome = input()
print("Digite a sua idade:")
idade = input()
print(nome)
print(idade)
print(type(nome))
print(type(idade))

#Saída:
# Digite o seu nome:
# Leo
# Digite a sua idade:
# 34
# Leo
# 34
# <class 'str'>
# <class 'str'>

#Exemplo C: como converter o valor obtido pelo comando input() para um tipo de interesse. Nesse exemplo a conversão foi feita para inteiro 'int'. Para
#realizar a conversão é necessário colocar a função input como parâmetro de uma função de conversão. Neste caso foi usada a função int().
numero = int(input('Digite um número: '))
print(numero)
print(type(numero))

#Saída:
# Digite um número: 8
# 8
# <class 'int'>

