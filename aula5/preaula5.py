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

P = int(input("Digite o primeiro termo: "))
R = int(input("Digite a razão: "))
Q = int(input("Digite a quantidade de termos da PA: "))
cont = 0
termo = 1
soma = 0
while cont < Q:       
    print("Termo {} da PA = {}".format(termo, P))
    P = P + R
    termo = termo + 1
    cont = cont + 1
    soma = soma + P
print("Somatório dos elementos da PA = {}".format(soma))


print("\n\n\nFim do programa")
