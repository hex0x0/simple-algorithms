

lista = [1, 2, 3, 3, 4, 5, 5, 5]
lista2 = lista


for ele in lista2:
    aparicao = lista.count(ele)
    for j in range(aparicao-1):
        lista.remove(ele)


print(lista)