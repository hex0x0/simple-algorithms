
"""

Lista é um valor que contém diversos valores em uma sequência ordenada
O termo valor de lista refere-se à lista propriamente dita

lista = [1, 2, 3]


print(lista[0:-2])

[1]


itens = ['buceta', 'cu', 'pinto de mel']

del itens[0]
print(itens)

O del apaga um valor num índice

Os valores na lista são deslocados em consequência disso

"""


def lista(n):
    if n == []:
        return

    #print(n)
    lista(n[2])

    

    lista(n[1])

    print(n[0], end=' ')




n6 = [4, [], []]
n5 = [6, [], n6]
n4 = [9, [], []]
n3 = [5, [], []]
n2 = [8, n5, []]
n1 = [7, n3, n4]
n0 = [3, n1, n2]

lista(n0)

