def lista():
    start = 0
    lista = []

    def incrementa(item):
        nonlocal lista, start
        lista.append(item)
        start+=1
        print(item, start)

    return incrementa


lista_compras = lista()

lista_compras('hiai')
lista_compras('poedrai')
