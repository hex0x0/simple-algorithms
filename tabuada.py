#aula40


def cria_tabuada(n):
    
    def tabuada(m):
        for i in range(n, m-1, -1):
            for j in range(1, 11):
                print('{} x {} = {}'.format(i, j, i*j))

    return tabuada



tab = cria_tabuada(3)

tab(1)
