'''
Escreva um programa que leia uma lista com N números inteiros, onde N é um número inteiro previamente
digitado pelo usuário. O programa não deve aceitar um número digitado que já esteja inserido na lista, sendo que
quando esta situação ocorrer uma mensagem deve ser dada ao usuário. Por fim exibir na tela a lista resultante.
'''

N = int(input("Digite o tamanho da lista: "))
A = []
TamA = 0 #tamanho da lista até o último elemento adicionado antes da quantidade total de elementos
i = 0

while i < N:
    x = int(input("Digite o elemento {} da lista: ".format(i)))
    jaEsta = False
    j = 0 #contador auxiliar para percorrer cada elemento da lista inda incompleta
    while j < TamA: #esse laço percorre a lista já existente para verificar se o elemento já está na lista
        if A[j] == x:
            jaEsta = True
        j += 1
    
    if not jaEsta:
        A.append(x)
        TamA += 1
        #i += 1 #este contador, se ativado, só avança quando o valor for inserido na lista
    else:
        print("     ...o valor {} já está na lista! Digite outro por favor.\n".format(x))
    i += 1   #esse contador se ativado sempre avançará, mesmo quando o valor não for inserido na lista


print("\nA lista A tem {} elementos:".format(len(A)))
print(A)

print("\n\nFim do Programa")