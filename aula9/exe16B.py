'''
Escreva um programa que leia uma lista com N números inteiros, onde N é um número inteiro previamente
digitado pelo usuário. O programa não deve aceitar um número digitado que já esteja inserido na lista, sendo que
quando esta situação ocorrer uma mensagem deve ser dada ao usuário. Por fim exibir na tela a lista resultante.
'''

def estaNaLista(valor, Lista, Tam): #o comando def nos permite criar uma função com operações que podemos aplicar ao longo do programa
    j = 0
    while j < Tam:
        if Lista[j] == valor:
            return True
        j += 1
    return False

N = int(input("Digite o tamanho da lista: "))
A = []
TamA = 0 #tamanho da lista até o último elemento adicionado antes da quantidade total de elementos
i = 0

while i < N:
    x = int(input("Digite o elemento {} da lista: ".format(i)))
    
    if estaNaLista(x, A, TamA):
        print("     ...o valor {} já está na lista! Digite outro por favor.\n".format(x))
    else:
        A.append(x)
        TamA += 1      
    i += 1   

print("\nA lista A tem {} elementos:".format(len(A)))
print(A)

print("\n\nFim do Programa")