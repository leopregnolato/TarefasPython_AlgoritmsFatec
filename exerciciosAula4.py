### Exercício 01

# X = int(input("Digite um número: "))
# if X > 0:
#     print("Maior que 0")

### Exercício 2

# A = int(input("Digite um número: "))
# B = int(input("Digite outro número: "))
# if A < B:
#     print(A)
# else:
#     print(B)

### Exercício 3

# A = int(input("Digite um número: "))
# B = int(input("Digite outro número: "))
# if A < B:
#     print("O menor número é", A, "e o maior número é", B)
# else:
#     print("O menor número é", B, "e o maior número é", A)

### Exercício 4

# A = int(input())
# if (A % 2) == 0:
#     print("O número", A, "é par.")
# else:
#     print("O número", A, "é ímpar.")

# ### Exercício 5 ****ENTREGA****

# A = int(input("Digite um número:"))
# if A > 0:
#     print("O número é positivo")
# elif A == 0:
#     print("O número é igual a zero")
# else:
#     print("O número é negativo")

# ### Exercício 6 ****ENTREGA****

# nome = input("Digite o nome do lutador: ")
# peso = float(input("Digite o peso do lutador: "))
# if peso < 65:
#     print("O lutador", nome, "pesa", peso, "kg e se enquadra na categoria Pena")
# elif peso >= 65 and peso < 72:
#     print("O lutador", nome, "pesa", peso, "kg e se enquadra na categoria Leve")
# elif peso >= 72 and peso < 79:
#     print("O lutador", nome, "pesa", peso, "kg e se enquadra na categoria Ligeiro")
# elif peso >= 79 and peso < 86:
#     print("O lutador", nome, "pesa", peso, "kg e se enquadra na categoria Meio Médio")
# elif peso >= 86 and peso < 93:
#     print("O lutador", nome, "pesa", peso, "kg e se enquadra na categoria Médio")
# elif peso >= 93 and peso < 100:
#     print("O lutador", nome, "pesa", peso, "kg e se enquadra na categoria Meio Pesado")
# else:
#     print("O lutador", nome, "pesa", peso, "kg e se enquadra na categoria Pesado")

# ### Exercício 7 ****ENTREGA****

# A = float(input("Digite o valor de A: "))
# B = float(input("Digite o valor de B: "))
# C = float(input("Digite o valor de C: "))

# delta = ((B ** 2) - (4 * A * C))

# if delta > 0:
#     x1 = ((-B) + (delta ** 0.5)) / (2 * A)
#     x2 = ((-B) - (delta ** 0.5)) / (2 * A)
#     print("As raízes da equação são", x1, "e", x2)
# elif delta == 0:
#     x = (-B) / (2 * A)
#     print("A raiz da equação é", x)
# else:
#     print("Não há raízes reais")

# ### Exercício 8 ****ENTREGA****


# A = int(input("Digite o 1º lado do triângulo: "))
# B = int(input("Digite o 2º lado do triângulo: "))
# C = int(input("Digite o 3º lado do triângulo: "))

# if (abs(B - C) < A < B + C) or (abs(A - C) < B < A + C) or (abs(A - B) < C < A + B):
#     if (A != B) and (A != C) and (B != C):
#         print("Tiângulo escaleno")
#     elif (A == B and B != C) or (A == B and A != C ) or (A == C and A != B):
#         print("Tiângulo isósceles")
#     elif (A == B and A == C) and B == C:
#         print("Tiângulo equilátero")
# else:
#     print("Não existe triângulo")



