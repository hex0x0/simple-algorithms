import random

def gera_numero():

    lista_numeros = list(range(1, 10))

    secretNum = 0 

    random.shuffle(lista_numeros)


    for i in range(4):
        dig = lista_numeros[i]
        secretNum += dig * (10 ** (3-i))

    print(secretNum)


gera_numero()

        




