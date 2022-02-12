def recebe_lista(*lista):
    aux=0
    for i in lista:
        aux+=i
    
    return aux


print(recebe_lista(1, 2, 3, 10, 9, 8))

