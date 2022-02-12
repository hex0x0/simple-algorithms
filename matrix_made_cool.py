import random

matrix = []
def create_matrix(n, m, matrix):
    for i in range(m):
        line = []
        for j in range(n):
            value = random.randint(1, 10)
            line.append(value)
        matrix.append(line)
    



def troca_posicao(p1, p2, matrix):  
    pos_1 = matrix[p1//10][p1%10]
    pos_2 = matrix[p2//10][p2%10]

    matrix[p1//10][p1%10] = pos_2
    matrix[p2//10][p2%10] = pos_1
        



create_matrix(3, 3, matrix)

print(matrix)

po1 = int(input('Digite a posicao 1: '))
po2 = int(input('Digite a posicao 2: '))

troca_posicao(po1, po2, matrix)


print(matrix)




