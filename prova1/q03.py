print("Daniel Marcionilo Pedroso do Rosario Silva, RA: 21206301")
print("Leonardo Antonio Pregnolato, RA: 21206393")
print("Questão 3")

NV = int(input("Digite a quantidade de vendas: "))

while NV <= 0:
    print("Valor inválido! Digite uma quantidade de vendas maior que zero!")
    NV = int(input("\nDigite a quantidade de vendas: "))

i = 0
L = []
totalA = 0
totalV = 0
vendaAtotal = 0
vendaVtotal = 0

while i < NV:
    venda = input("Digite o Codigo e a Quantidade: ")
    L = venda.split()
    Cod = int(L[0])
    QV = int(L[1])

    if Cod == 16:
        QMA = 50
        if QV <= QMA:
            totalV = QV * 14.35
            vendaVtotal = vendaVtotal + totalV
        else:
            totalA = QV * 12.93 
            vendaAtotal = vendaAtotal + totalA       

    elif Cod == 23:
        QMA = 100
        if QV <= QMA:
            totalV = QV * 35.12
            vendaVtotal = vendaVtotal + totalV
        else:
            totalA = QV * 29.85
            vendaAtotal = vendaAtotal + totalA
        
    elif Cod == 27:
        QMA = 70
        if QV <= QMA:
            totalV = QV * 19.35
            vendaVtotal = vendaVtotal + totalV
        else:
            totalA = QV * 16.76
            vendaAtotal = vendaAtotal + totalA
        
    elif Cod == 34:
        QMA = 40
        if QV <= QMA:
            totalV = QV * 63.40
            vendaVtotal = vendaVtotal + totalV
        else:
            totalA = QV * 58.25
            vendaAtotal = vendaAtotal + totalA

    else: 
        print("Código inválido!")
    i += 1

print("\n\nTotal de vendas do grupo varejo: R$ {:.2f}".format(vendaVtotal))
print("Total de vendas do grupo atacado: R$ {:.2f}".format(vendaAtotal))
print("\n\nVendas totais: R$ {}".format(vendaVtotal + vendaAtotal))
