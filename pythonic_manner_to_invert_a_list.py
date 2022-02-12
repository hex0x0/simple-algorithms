array = [4, 3, 1, 7, 3, 2, 1, 9]

aux = array[:]

b = []


while len(b) != len(array):
    menor  = aux[0]

    for ele in aux:
        if ele < menor:
            menor = ele
    

    b.append(menor)
    aux.remove(menor)

array = b


print(array)
