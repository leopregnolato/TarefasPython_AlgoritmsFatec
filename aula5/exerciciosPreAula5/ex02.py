number = 1
negative = 0
positive = 0
while number !=0:
    number = int(input("Digite um número: "))
    if number < 0:
        negative = negative + number
    elif number > 0:
        positive = positive + number
print("Total dos positivos: %d" % positive)
print("Total dos negativos: %d" % negative)