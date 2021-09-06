'''
Elaborar um programa que efetue a leitura de valores positivos inteiros até que zero ou um valor
negativo seja informado. Ao final devem ser apresentados: o maior e menor valores informados pelo
usuário, a quantidade de valores, a soma e a média de todos.
'''
N = int(input("Digite um número: "))
count = 0
numbers = []
sum = 0


while N > 0:    
    sum = sum + N
    count = count + 1    
    numbers.append(N)
    N = int(input("Digite um número: "))

orderednumbers = sorted(numbers)
minor = orderednumbers[0]
major = orderednumbers[count - 1]
mean = sum / count

print("O maior valor é: {}".format(major))
print("O menor valor é: {}".format(minor))
print("A quantidade de números digitados é: {}".format(count))
print("O somatório dos valores é: {}".format(sum))
print("A média é: {}".format(mean))
