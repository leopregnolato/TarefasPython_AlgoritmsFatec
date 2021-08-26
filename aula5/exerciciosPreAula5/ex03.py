N = int(input("Digite uma quantidade: "))
R = 0
sum = 0
count = 0
while count < N:
    R = float(input("Digite um valor real: "))
    sum = sum + R
    count = count + 1
print("A soma dos valores digitados é: %d" % sum)