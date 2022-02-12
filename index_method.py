array = [1, 2, 2, 3]


#use a built-in-function index






#devolve o indice


found = False
i = 0

x = int(input("Digite um numero:"))

while not found and i < len(array):
    if array[i]  == x:
        print('Elemento %i se encontra na posicao %i'%(x, i))
        found = True
    

    i+= 1


if not found:
    print('Não achei')



print('Elemento %i está na posicao %i'%(x, array.index(x)))