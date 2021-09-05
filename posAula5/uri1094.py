'''
Maria acabou de iniciar seu curso de graduação na faculdade de medicina e precisa de sua ajuda para organizar os experimentos de um laboratório o qual ela é responsável. Ela quer saber no final do ano, quantas cobaias foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada.

Este laboratório em especial utiliza três tipos de cobaias: sapos, ratos e coelhos. Para obter estas informações, ela sabe exatamente o número de experimentos que foram realizados, o tipo de cobaia utilizada e a quantidade de cobaias utilizadas em cada experimento.

Entrada
A primeira linha de entrada contém um valor inteiro N que indica os vários casos de teste que vem a seguir. Cada caso de teste contém um inteiro Quantia (1 ≤ Quantia ≤ 15) que representa a quantidade de cobaias utilizadas e um caractere Tipo ('C', 'R' ou 'S'), indicando o tipo de cobaia (R:Rato S:Sapo C:Coelho).

Saída
Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia utilizada e o percentual de cada uma em relação ao total de cobaias utilizadas, sendo que o percentual deve ser apresentado com dois dígitos após o ponto.
'''

N = int(input())
count = 0
casetest = []
numberused = 0
typeused = 0 
mean = 0
total = 0
rabbit = 0
mouse = 0
frog = 0
trabbit = 0
tmouse = 0
tfrog = 0

while count < N:
    casetest = input()
    casetest = casetest.split()
    numberused = int(casetest[0])
    typeused = casetest[1]
    total = total + numberused
    if typeused == "C" or typeused == "c":
        rabbit = rabbit + numberused
    elif typeused == "R" or typeused == "r":
        mouse = mouse + numberused
    elif typeused == "S" or typeused == "s":
        frog = frog + numberused
    count = count + 1

trabbit = ((rabbit * 100) / total)
tmouse = ((mouse * 100) / total)   
tfrog = ((frog * 100) / total)

print("Total: {} cobaias".format(total))
print("Total de coelhos: {}".format(rabbit))
print("Total de ratos: {}".format(mouse))
print("Total de sapos: {}".format(frog))
print("Percentual de coelhos: {:.2f} %".format(trabbit))
print("Percentual de ratos: {:.2f} %".format(tmouse))
print("Percentual de sapos: {:.2f} %".format(tfrog))   