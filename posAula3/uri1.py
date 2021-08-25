########## RAIO

# a = input()
# b = "{:.2f}".format(a)
# raio = float(b)

# from decimal import Decimal

# raio = float(input())
# pi = 3.14159
# area = pi * (raio ** 2)
# area = Decimal(area)
# print("A=%.4f" % area)


#print("A = %.4f \n" % area)
#print(area)
#print(type(area))
# raio = float(input("Digite: "))
# raio2 = "{:.2f}".format(raio)
# print(type(raio2))
# print(raio2)

####### ex 3 soma

# A = int(input())
# B = int(input())
# SOMA = A + B
# print("SOMA = %i" % SOMA)

# ### ex 4 Produto simples

# A = int(input())
# B = int(input())
# PROD = A * B
# print("PROD = %i" % PROD)

#### ex4 Media Simples - Media 1
# from decimal import Decimal

# A = float(input())
# B = float(input())
# MEDIA =((A * 0.35) + (B * 0.75)) * (10/11)
# MEDIA = Decimal(MEDIA)
# print("MEDIA = %.5f" % MEDIA)

# area = Decimal(area)
# print("A=%.4f" % area)

#ex7 Diferença

# A = int(input())
# B = int(input())
# C = int(input())
# D = int(input())
# DIFERENCA = (A * B - C * D)
# print("DIFERENCA = %i" % DIFERENCA)

## float com casas decimais

# from decimal import Decimal


# A = float(input("Ecreva um número: "))
# B = Decimal(format(A, '.4f'))
# #B = Decimal(A)
# print(B)
# print(type(B))

#### ex4 Media Simples - Media 2  - problema 1006

# from decimal import Decimal

# A = float(input())
# B = float(input())
# C = float(input())
# MEDIA =((A * 0.2) + (B * 0.3) + (C * 0.5))
# MEDIA = Decimal(MEDIA)
# print("MEDIA = %.1f" % MEDIA)

#### Salário  - problema 1008

# from decimal import Decimal

# NUMBER = int(input())
# HOURS = int(input())
# VALUE = float(input())
# SALARY = HOURS * VALUE
# SALARY = Decimal(SALARY)
# print("NUMBER = %i" % NUMBER)
# print("SALARY = U$ %.2f" % SALARY)

#### Salário com bonus - problema 1009

# from decimal import Decimal

# NAME = input()
# SALARY = float(input())
# SALES = float(input())
# GAIN = SALARY + (SALES * 0.15)
# GAIN = Decimal(GAIN)
# print("TOTAL = R$ %.2f" % GAIN)

### Calculo Simples problema 1010

from decimal import Decimal

# CODIGOA= int(input())
# QUANTIDADEA = int(input())
# VALORA = float(input())
# CODIGOB = int(input())
# QUANTIDADEB = int(input())
# VALORB = float(input())


A = input()
B = input()
CODIGOA, QUANTIDADEA, VALORA = A.split(" ")
CODIGOB, QUANTIDADEB, VALORB = B.split(" ")
CODIGOA = int(CODIGOA)
QUANTIDADEA = int(QUANTIDADEA)
VALORA = float(VALORA)
CODIGOB = int(CODIGOB)
QUANTIDADEB = int(QUANTIDADEB)
VALORB = float(VALORB)
TOTAL = ((QUANTIDADEA * VALORA) + (QUANTIDADEB * VALORB))
TOTAL = Decimal(TOTAL)
print("VALOR A PAGAR: R$ %.2f" % TOTAL)