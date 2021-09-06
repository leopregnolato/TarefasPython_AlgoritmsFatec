'''
Escreva um programa que apresente todos os valores inteiros divisíveis por 5 situados entre um valor
mínimo e um máximo, fornecidos pelo usuário. É obrigatório que o valor máximo seja maior que o
mínimo e se isso não ocorrer, deve ser dada uma mensagem de erro ao usuário.
'''
minnumber = int(input("Digite um número: "))
maxnumber = int(input("Digite um número maior que o anterior: "))
count = 0

if maxnumber < minnumber:
    print("Erro: você digitou o segundo número menor que o primeiro! Digite novamente por favor.")
else:    
    elements = maxnumber - minnumber
    number = minnumber
    while count < elements:         
        if number % 5 == 0:
            print(number)
        else:
            number = number
        count = count + 1
        number = number + 1
        

