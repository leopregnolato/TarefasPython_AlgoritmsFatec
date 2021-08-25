'''
Aumento de Salário
Por Neilor Tonin, URI  Brasil

A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:

Salário	Percentual de Reajuste
0 - 400.00          15%
400.01 - 800.00     12%
800.01 - 1200.00    10%
1200.01 - 2000.00   7%
Acima de 2000.00    4%

Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho 
e o índice reajustado, em percentual.
'''

salary = float(input())

if salary >= 0 and salary <= 400:
    earn = salary * 0.15   
    newSalary = salary + earn
    percentage = "15 %"
elif salary >= 400.01 and salary <= 800:
    earn = salary * 0.12   
    newSalary = salary + earn
    percentage = "12 %"
elif salary >= 800.01 and salary <= 1200:
    earn = salary * 0.10   
    newSalary = salary + earn
    percentage = "10 %"
elif salary >= 1200.01 and salary <= 2000:
    earn = salary * 0.07   
    newSalary = salary + earn
    percentage = "7 %"
elif salary >= 2000:
    earn = salary * 0.04  
    newSalary = salary + earn
    percentage = "4 %"

print("Novo salario: {:.2f}".format(newSalary))
print("Reajuste ganho: {:.2f}".format(earn))
print("Em percentual: {}".format(percentage))
