"""

Aula 28

Stand Users

"""
from itertools import count


votos = []
num_votos = 0
mais_votado = 0
parar = False

x = 0
while not parar:
    x = int(input("Type a number between 1 e 23 and -1 to finish this damn program: "))
    
    if x == -1:
        parar = True
    else:
        while x not in range(2, 23):
            x = int(input("Type that again, you fucking dork: "))

        print()
        votos.append(x)
        num_votos+=1

   



print(votos)

print(num_votos)

#imprir elementos sem repeticao


aux = votos.count(2)
pos = 0
for i in range(2, 23):
    if i in votos:
        print('O jogador {} teve {} votos'.format(i, votos.count(i)))

        if votos.count(i) > aux:
            pos = i
            aux = votos.count(i)


print()

print('O jogador {} foi o mais votado com {} votos'.format(pos, aux))





        
        

