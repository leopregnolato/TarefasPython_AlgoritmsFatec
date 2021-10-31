'''
Faça um programa que permaneça em laço até que seja digitado um valor menor ou igual a zero. Cada valor válido
(positivo) digitado deve ser inserido em uma lista na posição imediatamente antes do primeiro elemento que seja
maior que valor que está sendo inserido. Isso resultará em uma lista ordenada de forma crescente. Será
necessário usar o método insert da lista – pesquise sobre ele.
'''

N = int(input("Digite um valor: "))
L = []
tamL = 0

while N > 0:
    if tamL == 0:
       L.append(N)
       tamL += 1
    else:
        i = 0
        while i < len(L):
            if N < L[i]:
                L.insert(i, N)
                i += 1    
                tamL += 1            
            elif N == L[0]:                
                print("{} já está na lista! Digite outro valor!".format(N))
            elif N > L[i]:
                
    N = int(input("Digite outro valor: "))




if tamL == 0:
    print("\nNão foi gerada lista.")
else:
    print("\n\nA lista gerada possui {} elementos:".format(tamL))
    print(L)

print("\n\nFim do programa.")



