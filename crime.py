respostas=[]


respostas.append(int(input("Telefonou para a vítima: (1 - sim ou 0 - Não")))
respostas.append(int(input("Esteve no local do crime: (1 - sim ou 0 - Não")))
respostas.append(int(input("Mora perto da vítima: (1 - sim ou 0 - Não")))
respostas.append(int(input("Devia para a vítima: (1 - sim ou 0 - Não")))
respostas.append(int(input("Já trabalhou com a vítima: (1 - sim ou 0 - Não")))

soma_repostas=0


for r in respostas:
    soma_repostas+=r


if soma_repostas < 2:
    print('Inocente')
elif soma_repostas == 2:
    print('Suspeita')
elif soma_repostas <=4:
    print('Cumplice')
else:
    print('Assassino')
