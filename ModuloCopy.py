import copy

#se houver listas internas, use copy.deepcopy()

lista = ['a', 'b','c']



lista2 = copy.copy(lista)


lista2[2] = '22'


print(lista2)