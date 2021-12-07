print("Daniel Marcionilo Pedroso do Rosario Silva, RA: 21206301")
print("Gustavo Notarnicola Gonçalves, RA: 21206464")
print("Leonardo Antonio Pregnolato, RA: 21206393")
print("N2D\n\n")

def estaNaLista(valor, Lista, Tam): #o comando def nos permite criar uma função com operações que podemos aplicar ao longo do programa
    j = 0
    while j < Tam:
        if Lista[j] == valor:
            return True
        j += 1
    return False

'''
while i < N:
    x = int(input("Digite o elemento {} da lista: ".format(i)))
    
    if estaNaLista(x, A, TamA):
        print("     ...o valor {} já está na lista! Digite outro por favor.\n".format(x))
    else:
        A.append(x)
        TamA += 1      
    i += 1   

print("\nA lista A tem {} elementos:".format(len(A)))
print(A)

print("\n\nFim do Programa")'''


#Vendas


Arq = open("c1_vendas.txt", "r")
Vendas = []

L = Arq.readline()
L = L.strip()

while L != '':
    L = L.split(";")
    Vendas.append(L)
    L = Arq.readline()
    L = L.strip()
Arq.close()
#print(Vendas)

i = 0
j = 0
A = 0
vendasCodigo = []
x = 0
qtVendas = []
somaVendas = 0


'''if estaNaLista(x, A, TamA):
    print("     ...o valor {} já está na lista! Digite outro por favor.\n".format(x))
else:'''
         
    




while i < len(Vendas):
    x = Vendas[i][0]
    j = len(Vendas) - i 
    while j > 0:       
        z = Vendas[j-1][1]
        w = int(Vendas[j-1][2])
        if Vendas[j-1][0] == x:
            if w == 100 or w == 102:            
                A = int(z)
                somaVendas = somaVendas + A
        j -= 1                            
    i += 1 
    qtVendas.append(x)
    qtVendas.append(somaVendas)
    
    somaVendas = 0
    
    
    

print(qtVendas)




'''
VendasProdutoX = []
while L != "":
    Codigo = int(L[0])
    Quantidade = int(L[1])
    Preco = float(L[2])
    
'''



    

    
#FILTROS

# cod produto

#situação de venda


                    #L[0], L[1] e L[2] puderam se identificados como Código, Quantidade e Preço, respectivamente.
'''  
L = L.split(";") #Cada elemento da lista foi transformado com o split baseado no separador ";" em um elemento de uma segunda lista L. Desse modo, os elementos
 
Total = Total + (Quantidade * Preco)
qtdeTotal = qtdeTotal + Quantidade
dados.append([Codigo , Quantidade, Preco])
L = Arq.readline()


#produtos
Arq = open("c1_produtos.txt", "r")
Produtos = []

L = Arq.readline()
L = L.strip()

while L != '':
    L = L.split(";")    
    Produtos.append(L)
    L = Arq.readline()
    L = L.strip()
    
Arq.close()
print(Produtos)





arquivo = open("TRANSFERE.txt", "w", encoding="utf-8")


arquivo.write("Necessidade de Transferência Armazém para CO\n\n")
A = "Produto"
B = "QtCO"
C = "QtMin"
D = "QtVendas"
E = "Estq. após Vendas"
F = "Necess. Transf. de Arm p/ CO"

arquivo.write(f"{A: >15}{B: >15}{C: >15}{D: >15}{E: >35}{F: >35}\n")


arquivo.close()

#arquivo.write(f"{PBruto: >10.2f}{PAliqINSS: >15.1f}{PValINSS: >15.2f}{PBaseIR: >15.2f}{PAliqIR: >15.1f}{PValIR: >15.2f}{PSalLiquido: >15.2f}\n")

'''

print("\n\nFim do Programa")