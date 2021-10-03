'''Leia dois números inteiros LMin e LMax. Em seguida leia 10 valores inteiros e inserindo-os em uma lista A somente
se o valor fornecido estiver no intervalo [LMin, LMax]. Valores fora deste intervalo devem ser ignorados. Ao final,
apresentar a lista A e seu tamanho efetivo. Observe que para este programa funcionar apropriadamente é
necessário que LMin seja menor que LMax. Caso o usuário digite LMax menor que LMin, o programa deve inverter
os valores. Colocar este programa no site do professor.
'''

LMin = int(input("Digite um valor mínimo: "))
LMax = int(input("Digite um valor máximo: "))

if LMax < LMin:
    X = LMax
    LMax = LMin
    LMin = X

A = []
count = 0

while count < 10:
    N = int(input("Digite o {}° valor: ".format(count + 1)))
    if N >= LMin and N <=LMax:
        A.append(N)
        count = count + 1
    else:
        print("Valor {} fora do intervalo {} - {}!".format(N, LMin, LMax))

Alenght = len(A)

print("\nResultados:")
print("-----------------------------------------------------------------------------------------")
print("     Lista informada: {}".format(A))
print("     Quantidade de valores: {}".format(Alenght))
print("-----------------------------------------------------------------------------------------")
print("\n\nFim do programa")