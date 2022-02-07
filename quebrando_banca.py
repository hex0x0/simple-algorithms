import random


n_testes = int(input("Digite o número de testes:"))

trocar = 0
n_trocar = 0

for i in range(n_testes):
    porta = random.randrange(1, 4)
    premio = random.randint(1, 3)

    if porta == premio:
        n_trocar+=1
    else:
        trocar+= 1


print("É vantajoso trocar a porta {:.2f}".format(trocar*100/n_testes))
print("Não é vantajoso trocar a porta {:.2f}".format(n_trocar*100/100))
