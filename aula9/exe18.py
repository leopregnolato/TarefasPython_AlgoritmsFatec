'''
O programa deverá ler dois inteiros chamados Min e Max. Min pode ser qualquer valor e Max, obrigatoriamente,
deve ser maior que Min. Em seguida preencher a lista com todos os valores situados entre Min e Max que sejam
divisíveis por 7. Exibir a lista resultante na tela.
'''

Min = int(input("Digite Min: "))
Max = int(input("Digite Max: "))

L = []
a = Min
while a <= Max:
    if a % 7 == 0:
        L.append(a)
    a += 1

print("\nLista L contém {} elementos:".format(len(L)))
print(L)

print("\n\nFim do Programa")