print("Daniel Marcionilo Pedroso do Rosario Silva, RA: 21206301")
print("Gustavo Notarnicola Gonçalves, RA: 21206464")
print("Leonardo Antonio Pregnolato, RA: 21206393")
print("N2A\n\n")

Arq = open("vendas.txt", "r") 
qtdeTotal = 0
Total = 0
dados = []
L = Arq.readline()
while L != "": #Percorremos o arquivo e cada linha foi transformada em um elemnto da lista (lista "dados")
    L = L.split(";") #Cada elemento da lista foi transformado com o split baseado no separador ";" em um elemento de uma segunda lista L. Desse modo, os elementos
                    #L[0], L[1] e L[2] puderam se identificados como Código, Quantidade e Preço, respectivamente.
    Codigo = int(L[0])
    Quantidade = int(L[1])
    Preco = float(L[2])
    Total = Total + (Quantidade * Preco)
    qtdeTotal = qtdeTotal + Quantidade
    dados.append([Codigo , Quantidade, Preco])
    L = Arq.readline()

print("\nA quantidade vendida foi de {} produtos, totalizando R$ {:.2f}".format(qtdeTotal, Total))

S = int(input("\nDigite o código: "))
i = 0

Total = 0

while S != 0:
    if S < 10000 or S > 21000:
        print("\n{} Código inválido (deve ser entre 10000 e 21000)".format(S))
    else:
        while i < len(dados):
            if int(dados[i][0]) == S:
                Quantidade = int(dados[i][1])
                Preco = float(dados[i][2])
                Total = Total + (Quantidade * Preco)   
            i = i + 1
              
        print("\nTotal vendido do produto {} = R$ {:.2f}".format(S, Total))
    
    i = 0
    Total = 0
    S = int(input("\nDigite o código: "))

Arq.close()

print("\n\nFim do programa.")
