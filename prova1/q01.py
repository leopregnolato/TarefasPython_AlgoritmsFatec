print("Daniel Marcionilo Pedroso do Rosario Silva, RA: 21206301")
print("Leonardo Antonio Pregnolato, RA: 21206393")
print("Questão 1\n\n")

'''
Escreva um programa que leia um número inteiro que representa a quantidade de segundos que foram consumidos para realizar
uma determinada tarefa. Em seguida mostre esse tempo na tela no formato:
X horas, Y minutos, Z segundos
'''
print("Calculadora do tempo!\n")
N = int(input("Digite o tempo em segundos: "))

horas = N // 3600
minutosEmSegundos = N % 3600
minutos = minutosEmSegundos // 60
segundos = N % 60

print("\n{} horas, {} minutos, {} segundos".format(horas, minutos, segundos))
print("\n\nFim do programa.")

