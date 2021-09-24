'''
Refaça o programa anterior, porém ao final exiba na tela cada elemento da lista em uma linha da tela
(este programa deve exibir um elemento por vez dentro de um laço e usando um índice para acessar
cada elemento individualmente).
'''

N = float(input("Digite um número: "))
L = []
i = 0
count = 0

while N > 0:
    L.append(N)
    count = count + 1
    N = float(input("Digite um número: "))

while i < count:
    print(L[i])
    i = i + 1

print("\n\nFim do programa")