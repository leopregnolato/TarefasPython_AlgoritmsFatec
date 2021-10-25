###################################################################################### 
###   BUSCA LINEAR OU BUSCA SEQUENCIAL (DO PRIMEIRO AO ÚLTIMO)
###################################################################################### 

contEliminados = 0
i = 0

while i < N:
    if A[i] == X:
        contEliminados += 1
        print("     encontrado na posição {} - ELIMINADO".format(i))
        del(A[i])
        N = N - 1 
    else:
        i += 1

if contEliminados > 0:
    print("     Foram eliminados {} elementos".format(contEliminados))
    print("\n\nLista após a eliminação de {}".format(X))
    print(A)
else:
    print("     Não houve eliminados já que {} não está na lista.".format(X))
    
    
###################################################################################### 
###   BUSCA LINEAR OU BUSCA SEQUENCIAL (DO ÚLTIMO AO PRIMEIRO)
###################################################################################### 


contEliminados = 0
i = N - 1 #para começar no fim da lista

while i >= 0:
    if A[i] == X:
        contEliminados += 1
        print("     encontrado na posição {} - ELIMINADO".format(i))
        del(A[i])
        N = N - 1 #tirar um da lista para ajustar o tamanho da mesma após a eliminação
    i = i - 1
    

###################################################################################### 
###   CRIANDO E POPULANDO UMA LISTA COM NÚMEROS ALEATÓRIOS
###################################################################################### 

from random import randint

N = int(input("Digite o tamanho da lista: "))

A = []
count = 0

while count < N:
    B = randint(0, 10)
    A.append(B) 
    count = count + 1   


###################################################################################### 
###   RETIRADA DE REPETIDOS DEIXANDO APENAS A PRIMEIRA OCORRÊNCIA (BUSCA SEQUENCIAL + WHILE ADICIONAL)
###################################################################################### 


ContEliminados = 0
ref = 0 #ref representará a posição do elemento a partir do início da lista a ser comparado 
		#a outro a partir do final indicado por i 
		
while ref < N - 1: # N é o tamanho da lista
    i = N - 1 #i é o marcador do final para o começo da lista
    while i > ref:     # Busca sequencial aninhada em um laço que percorre toda a lista LAÇO ADICIONAL
        if L[ref] == L[i]: # o enésimo é igual ao 1°?, o enésimo é igual ao 2°? ...
            ContEliminados += 1
            del(L[i])
            N = N - 1
        i = i - 1

    ref += 1 #o ref só vai para o próximo depois que i percorrer a lista toda de trás para frente
    

###################################################################################### 
###   ADICIONANDO N PRIMOS EM UMA LISTA DE TAMANHO N
###################################################################################### 


candidatoPrimo = 2 #primeiro primo
i = 0 #índice da lista

while i < N:
    cont = 0
    j = 2 #será o possível divisor do candidatoPrimo, se dividir, candidatoPrimo não é primo (Resto == 0)
    while j < candidatoPrimo: #na primeira rodada não entra aqui para que 2 seja adicionado a lista
        Resto = candidatoPrimo % j
        if Resto == 0:
            cont += 1 # mudar o valor de cont fará com que o candidatoPrimo não seja adicionado na lista
        j += 1 #verifica o próximo valor < que candidatoPrimo como próximo possível divisor
    if cont == 0:
        L.append(candidatoPrimo)
        i += 1
    candidatoPrimo += 1


###################################################################################### 
###   JUNÇÃO DE DUAS LISTAS SEM CONCATENAÇÃO
###################################################################################### 

nR = nA + nB #Onde nA e nB são o tamanho de cada lista a ser juntada na lista R de tamanho nR
R = []
i = 0

while i < nA: #primeiro acrescenta-se todos os elementos de A
    R.append(A[i])
    i += 1

i = 0
while i < nB: #depois adiciona-se os elementos de B depois do último de A
    R.append(B[i])
    i += 1


###################################################################################### 
###   DEFININDO FUNÇÕES COM DEF
###################################################################################### 

#Ex 01

def NomeDaFuncao(parametro1, parametro2, parametro3): #os parâmetros podem ser qualquer valor (string, número ou lista)
    parametro3 = parametro1 * parametro2
    print("O resultado da multiplicação é {}".format(parametro3))

#Ex 02

def estaNaLista(valor, Lista, Tam): #o comando def nos permite criar uma função com operações que podemos aplicar ao longo do programa
    j = 0
    while j < Tam:
        if Lista[j] == valor:
            return True
        j += 1
    return False


###################################################################################### 
###   ADICIONANDO ELEMENTOS NA LISTA NA ORDEM INVERSA DE LEITURA
###################################################################################### 

L = []
count = 0

while count < 10:
    N = float(input("Digite um número: "))
    L.insert(0, N)
    count = count + 1

###################################################################################### 
###   EXIBINDO CADA ITEM DE UMA LISTA EM UMA LINHA
###################################################################################### 

L = []
i = 0
count = 0

while i < count:
    print(L[i])
    i = i + 1

###################################################################################### 
###   SALVANDO A SAÍDA DO PROGRAMA EM UM ARQUIVO TXT
###################################################################################### 

arquivo = open('NomeDoArquivo.txt', 'w')
#programa
arquivo.write("*** Tabuada do {}: ***\n\n".format(N)) # "Título" ou cabeçário do arquivo
#programa
#programa
#programa
arquivo.close() #deve ser a ultima linha do programa

###################################################################################### 
###   EXIBINDO A O MENOR E O MAIOR VALOR SEM LISTA E SEM SORT
###################################################################################### 

N = int(input('Digite N: '))
i = 0
while i < N:
    X = float(input('  digite o elemento {}: '.format(i)))

    # if para identificar o menor valor
    if i == 0 or X < CtrlMenor:
        CtrlMenor = X   
    # if para identificar o maior valor
    if i == 0 or X > CtrlMaior:
        CtrlMaior = X
        
    i = i + 1
    

###################################################################################### 
###   CRIANDO SOMATÓRIO
###################################################################################### 

N = int(input("Digite um número maior ou igual a 100: "))
count = 0
sum = 0
total = 0

if N >= 100:
    while count < N:
        sum = sum + 2
        total = total + sum
        count = count + 2
    print("Somatório: {}".format(total))
else:
    print("Número inválido")


###################################################################################### 
###   GARANTINDO O N CORRETO
###################################################################################### 

N = int(input("Digite N: "))

while N < 100:
    print("{} é inválido. Deve ser > 100".format(N))
    N = int(input("Digite N: "))

###################################################################################### 
###   SABER SE O NÚMERO É PRIMO
###################################################################################### 


N = int(input("Digite N para saber se é primo: "))

Cont = 0
i = 2
while i < N:
    Resto = N % i
    if Resto == 0:
        print("  {} é divisível por {}".format(N, i))
        Cont = Cont + 1
    i = i + 1

if Cont > 0:
    print("\n\n{} não é primo".format(N))
else:
    print("\n\n{} é primo".format(N))


###################################################################################### 
###   CRIANDO UMA PROGRESSÃO GEOMÉTRICA
###################################################################################### 


P = int(input("Digite o primeiro termo da PG: "))
R = int(input("Digite a razão da PG: "))
N = int(input("Digite o n° de termos da PG: "))
count = 0
while count < N:
    print(P)
    P = P * R
    count = count + 1


###################################################################################### 
###   VERIFICANDO SE UM NÚMERO É PAR
###################################################################################### 

N = int(input("Digite N: "))
resto = N % 2
if resto == 0:
    print("{} é par".format(N))
else:
    print("{} é ímpar".format(N))


###################################################################################### 
###   CLASSIFICANDO UM VALOR EM UMA ESCALA DE FAIXAS DE VALORES
###################################################################################### 

Nome = input("Digite o nome: ")
Peso = float(input("Digite o peso: "))
if Peso < 65:
    Categoria = "Pena"
elif Peso < 72:
    Categoria = "Leve"   
elif Peso < 79:
    Categoria = "Ligeiro"
elif Peso < 86:
    Categoria = "Meio médio"
elif Peso < 93:
    Categoria = "Médio"
elif Peso < 100:
    Categoria = "Meio pesado"
else:
    Categoria = "Pesado"
print("O lutador {} pesa {:.1f} kg e se enquadra na categoria {}".format(Nome, Peso, Categoria))
