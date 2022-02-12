#jogo megasena

#feito por mim x para mim
import random

jogo_competidor = random.sample(list(range(1, 61)), 6)

print('Seu jogo: {}'.format(jogo_competidor))

megasena = list(range(1, 61))



mega_aux = megasena.copy()


sorteio = []


while jogo_competidor != sorteio:
    sorteio = []
    for i in range(7):
        sorteado = random.choice(mega_aux)
        print(sorteio)
        sorteio.append(sorteado)

    sorteio.sort()



