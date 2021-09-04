'''
Leia um valor inteiro N. Este valor será a quantidade de valores inteiros X que serão lidos em seguida.
Mostre quantos destes valores X estão dentro do intervalo [10,20] e quantos estão fora do intervalo, mostrando essas informações.

Entrada
A primeira linha da entrada contém um valor inteiro N (N < 10000), que indica o número de casos de teste.
Cada caso de teste a seguir é um valor inteiro X (-10^7 < X <1^07).
 

Saída
Para cada caso, imprima quantos números estão dentro (in) e quantos valores estão fora (out) do intervalo.
'''

N = int(input())
count = 0
enter = 0
inside = 0
outside = 0

while count < N:
    enter = int(input())
    if enter >= 10 and enter <= 20:
        inside = inside + 1
    else:
        outside = outside + 1
    count = count + 1

print("{} in".format(inside))
print("{} out".format(outside))
