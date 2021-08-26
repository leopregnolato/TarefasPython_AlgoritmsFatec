P = int(input("Digite o primeiro termo da PG: "))
R = int(input("Digite a razão da PG: "))
N = int(input("Digite o n° de termos da PG: "))
count = 0
while count < N:
    print(P)
    P = P * R
    count = count + 1

