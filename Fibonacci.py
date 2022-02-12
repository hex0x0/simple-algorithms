f1 = 1
f2 = 0

aux = 0


for i in range(100):
    aux = f1 + f2
    f2 = f1
    f1 = aux
    print(aux)





