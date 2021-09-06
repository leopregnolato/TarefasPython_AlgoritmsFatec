'''
Reescreva um programa do exercício acima considerando exclusivamente os números positivos
fornecidos. Caso seja digitado zero ou um valor negativo o programa deve exibir uma mensagem
"número inválido" e o valor deve ser ignorado.
'''

N = int(input("Digite um número: "))
count = 0
numbers = []
minor = 0
major = 0
item = 0
valid = 0


while count < N:
        item = float(input("Digite o {}º número real: ".format(count +1)))
        if item > 0:
            numbers.append(float(item))
            valid = valid + 1
        else:
            print("Número inválido")
        count = count + 1

orderednumbers = sorted(numbers)

minor = orderednumbers[0]
major = orderednumbers[valid - 1]

print("O menor número é {}".format(minor))
print("O maior número é {}".format(major))