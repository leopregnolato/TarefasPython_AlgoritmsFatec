#Laços de repetição ou loops

# cont = 1

# while cont <= 10:
#     print(cont)
#     cont = cont + 1

# print("\n\n\nFim do programa")

# P = int(input("Digite o primeiro termo: "))
# R = int(input("Digite a razão: "))
# cont = 0
# while cont < 10:
#     print(P)
#     P = P + R
#     cont = cont + 1

# print("\n\n\nFim do programa")

# P = int(input("Digite o primeiro termo: "))
# R = int(input("Digite a razão: "))
# Q = int(input("Digite a quantidade de termos da PA: "))
# cont = 0
# termo = 1
# soma = 0
# while cont < Q:       
#     print("Termo {} da PA = {}".format(termo, P))
#     P = P + R
#     termo = termo + 1
#     cont = cont + 1
#     soma = soma + P
# print("Somatório dos elementos da PA = {}".format(soma))


# print("\n\n\nFim do programa")


# X = 1
# while X != 0:
#     X = int(input("Digite X: "))
#     if X % 2 == 0:
#         print("%d é par" % X)
#     else:
#         print("%d é ímpar" % X)

soma = 0
qtde = 0
X = 1
while X != 0:
    X = int(input("Digite X: "))
    if X != 0:
        soma = soma + X
        qtde = qtde +1

print("Total dos valores digitados = %d" % soma)
print("Quantidade de valores = %d" % qtde)