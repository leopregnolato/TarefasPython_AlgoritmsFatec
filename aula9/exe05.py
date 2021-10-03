'''Escreva um programa que leia um número N (obrigatoriamente entre 0 e 50 – o programa deve garantir isso em
um laço) e em seguida leia N números reais em uma lista A. O programa deve separar os valores lidos em A em
outras duas listas NEG e POS, a primeira contendo somente os valores negativos e a segunda contendo os valores
positivos e zero. Apresentar na tela as listas NEG e POS e a quantidade de valores contidos em cada uma. Colocar
este programa no site do professor.
'''

N = int(input("Digite um valor de 0 a 50: "))
count = 0
A = []
NEG = []
POS = []

while N <= 0 or N >=50:
    print("Você digitou um número fora do intervalo permitido.") 
    N = int(input("Digite um valor de 0 a 50: "))

while count < N:
    M = int(input("Digite o {}° número: ".format(count + 1)))
    A.append(M)
    count = count + 1

for M in A:
    if M < 0:
        NEG.append(M)
    if M >= 0:
        POS.append(M)

lenghtNEG = len(NEG)
lenghtPOS = len(POS)

print("\nResultados:")
print("-----------------------------------------------------------------------------------------")
print("     Lista de números positivos: {}".format(POS))
print("     Quantidade de valores: {}".format(lenghtPOS))
print("-----------------------------------------------------------------------------------------")
print("     Lista de números negativos: {}".format(NEG))
print("     Quantidade de valores: {}".format(lenghtNEG))
print("-----------------------------------------------------------------------------------------")
print("\n\nFim do programa")
    
