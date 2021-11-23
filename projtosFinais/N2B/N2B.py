print("Daniel Marcionilo Pedroso do Rosario Silva, RA: 21206301")
print("Gustavo Notarnicola Gonçalves, RA: 21206464")
print("Leonardo Antonio Pregnolato, RA: 21206393")
print("N2B\n\n")

import random

def GeraSenha(Tipo, Tamanho):
    Tipo = Tipo.lower()
    if Tipo == "a":
        s = ""
        i = 0
        while i < Tamanho:
            caractere = random.choice("0123456789")
            s = s + caractere
            i += 1
        return s
    elif Tipo == "b":
        s = ""
        i = 0
        while i < Tamanho:
            caractere = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
            s = s + caractere
            i += 1
        return s       
    elif Tipo == "c":
        s = ""
        i = 0
        while i < Tamanho:
            caractere = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
            s = s + caractere
            i += 1
        return s          
    elif Tipo == "d":
        s = ""
        i = 0
        while i < Tamanho:
            caractere = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789")
            s = s + caractere
            i += 1
        return s 
    elif Tipo == "e":
        s = ""
        i = 0
        while i < Tamanho:
            caractere = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_:@#$&?")
            s = s + caractere
            i += 1
        return s 
    return s

def Validation(x):
    x = x.lower()
    if x == "a":
        return True
    if x == "b":
        return True
    if x == "c":
        return True
    if x == "d":
        return True
    if x == "e":
        return True
    return False 

print("GERADOR DE SENHAS")
print("\nPor favor escolha uma das opções abaixo para gerar a sua senha:")
print("     a. Numérica – conterá apenas algarismos;")
print("     b. Alfabética – conterá apenas letras maiúsculas e minúsculas;")
print("     c. Alfanumérica 1 – conterá letras maiúsculas e algarismos;")
print("     d. Alfanumérica 2 – conterá letras maiúsculas, minúsculas e algarismos;")
print("     e. Geral – conterá letras maiúsculas, minúsculas, algarismos e os caracteres - _ : @ # $ & ?")

A = input("\nDigite a letra correspondente a sua opção: ")

while not Validation(A):
    print("\n...Valor inválido! Por favor digite uma letra entre A e E.")
    A = input("Digite a letra correspondente a sua opção: ")    

B = int(input("\nDigite o tamanho que a sua senha deve ter (número de caracteres): "))

Mat = []
Arq = open("MATR.txt", "r")
L = Arq.readline()

while L != '':
    Mat.append(L)
    L = Arq.readline()

Arq.close()

arquivo = open('SENHAS.txt', 'w')
i = 0

while i < len(Mat):
    m = Mat[i]
    m = m.strip()
    s = GeraSenha(A, B)        
    arquivo.write("{};{};\n".format(m, s))
    i += 1
    
arquivo.close()
print("\n\nFim do programa")
