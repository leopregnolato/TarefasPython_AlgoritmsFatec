print("Daniel Marcionilo Pedroso do Rosario Silva, RA: 21206301")
print("Gustavo Notarnicola Gonçalves, RA: 21206464")
print("Leonardo Antonio Pregnolato, RA: 21206393")
print("N2C\n\n")


def CalcAliqINSS(SalBruto):    
    if S <= 1751.81:        
        AliqINSS = 0.08        
    elif S >= 1751.82 and S <= 2919.72:       
        AliqINSS = 0.09        
    elif S >= 2919.73 and S <= 5839.45:
        AliqINSS = 0.11
    elif S >= 5839.46:
        AliqINSS = 1
    SalBruto = S
    return SalBruto, AliqINSS
  
def CalcValINSS(SalBruto, AliqINSS):
    ValINSS =  SalBruto * AliqINSS
    return ValINSS    


def CalcAliqIR(SalBruto, ValINSS):
    base = SalBruto - ValINSS
    if base <= 1903.98:        
        AliqIR = 0
        deducao = 0
    elif base >= 1903.99 and S <= 2826.65:       
        AliqIR = 0.075
        deducao = 142.8
    elif base >= 2826.66 and S <= 3751.05:
        AliqIR = 0.15
        deducao = 354.80
    elif base >= 3751.06 and S <= 4664.68:
        AliqIR = 0.225
        deducao = 636.13
    elif S >= 4664.69:
        AliqIR = 1
        deducao = 869.36
    return base, AliqIR, deducao

def CalcValIR(SalBruto, ValINSS, AliqIR, deducao):
    ValIR = ((SalBruto - ValINSS)  * AliqIR) - deducao
    if ValIR <= 10.00:
           ValIR = 0
    return ValIR

def CalcSalLiquido(SalBruto, ValINSS, ValIR):
    SalLiquido = SalBruto - ValINSS - ValIR
    return SalLiquido

SalBruto = 0
AliqINSS = 0
ValINSS = 0
AliqIR = 0
deducao = 0
ValIR = 0
SalLiquido = 0
base = 0

Arq = open("testepdf.txt", "r")

Salario = []

L = Arq.readline()
L = L.strip()

while L != '':
    Salario.append(L)
    L = Arq.readline()
    L = L.strip()

Arq.close()

arquivo = open("CALCULOS.txt", "w")

A = "Bruto" 
B = "AliqINSS"
C = "ValINSS"
D = "BaseIR"
E = "AliqIR"
F = "ValIR"
G = "SalLiquido"


arquivo.write(f"{A: >10}{B: >15}{C: >15}{D: >15}{E: >15}{F: >15}{G: >15}\n")

i = 0
while i < len(Salario):
    S = Salario[i]
    S = float(S)
    PBruto, PAliqINSS = CalcAliqINSS(S)
    PValINSS = CalcValINSS(PBruto, PAliqINSS)
    PBaseIR, PAliqIr, PDeducao = CalcAliqIR(PBruto, PValINSS)
    PValIR = CalcValIR(PBruto, PValINSS, PAliqIr, PDeducao) 
    PSalLiquido = CalcSalLiquido(PBruto, PValINSS, PValIR)
    PAliqINSS = PAliqINSS * 100
    PAliqIr = PAliqIr * 100    
    arquivo.write(f"{PBruto: >10.2f}{PAliqINSS: >15.1f}{PValINSS: >15.2f}{PBaseIR: >15.2f}{PAliqIr: >15.1f}{PValIR: >15.2f}{PSalLiquido: >15.2f}\n")
    i = i + 1
    
arquivo.close()
print("Arquivo exportado: CALCULOS.TXT")
print("\n\nFim do programa.")
