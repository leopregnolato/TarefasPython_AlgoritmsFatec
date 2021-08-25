'''
Leia um número inteiro que representa um código de DDD para discagem interurbana. Em seguida, informe à qual cidade o DDD pertence, considerando a tabela abaixo:

Se a entrada for qualquer outro DDD que não esteja presente na tabela acima, o programa deverá informar:
DDD nao cadastrado

Entrada
A entrada consiste de um único valor inteiro.
'''

code = int(input())

if code == 61:
    print("Brasilia")
elif code == 71:
    print("Salvador")
elif code == 11:
    print("Sao Paulo")
elif code == 21:
    print("Rio de Janeiro")
elif code == 32:
    print("Juiz de Fora")
elif code == 19:
    print("Campinas")
elif code == 27:
    print("Vitoria")
elif code == 31:
    print("Belo Horizonte")
else:
    print("DDD nao cadastrado")