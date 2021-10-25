'''. Escreva um programa que leia um número inteiro N e preencha uma lista com N elementos inteiros gerados
aleatoriamente entre 0 e 1000 (usar a função randint da biblioteca random). Exiba na tela a lista gerada. Em
seguida, o programa deve ler um valor X e informar se tal valor está, ou não está presente, bem como informar a
posição de X na lista. Se houver mais de uma ocorrência de X na lista informe todas as posições. Neste exercício
não é permitido usar os operadores in e not in. Também não é permitido usar qualquer função pronta de Python.'''

from random import randint

N = int(input("Digite o tamanho da lista: "))

A = []
count = 0

while count < N:
    B = randint(0, 1000)
    A.append(B) 
    count = count + 1    

print("-----------------------------------------------------------------------------------------")
print("Lista gerada: {}".format(A))
print("-----------------------------------------------------------------------------------------")

X = int(input("Digite um valor: "))
print("\nProcurando {} na lista...".format(X))
i = 0
achei = False

while i < N:
    if X == A[i]:
        achei = True
        print("     econtrado na posição {}".format(i))
    i = i + 1

if not achei:
    print("     não encontrado")

print("\n\nFim do programa")