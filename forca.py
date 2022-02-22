#hangman
import random
steps = [
     """
        +-----
        |
       ===
    """,
    
    """
        |
        0
        
       ===
    """,
    
    """
        0
       /|
       ===
    """,
    
    
    """
        0
       /|\
       ===
    """,
    
    """
        0
       /|\  
       / 
       ===
    """,
       
    """
        0
       /|\
       / \
       ===
    """
]

palavras = 'elefante pedra arroz verde azul branco'.split()


def main():
    #funcao principal do programa
    global steps
    
    print('HANGMAN')
    letrasErradas = ''
    letrasCertas = ''
    palavraSecreta = random_word().upper()
    
    
    jogando = True
    
    while jogando:
        printGame(letrasErradas, letrasCertas, palavraSecreta)
        
        guess = valid_guess(letrasCertas + letrasErradas)
        
        if guess in palavraSecreta:
            letrasCertas += guess

            if verifica_se_ganhou(palavraSecreta, letrasCertas):
                print('Exato! A palavra secreta é ' + palavraSecreta)
                jogando = False
                
        else:
            letrasErradas += guess

            if len(letrasErradas) == len(steps) -1:
                printGame(letrasErradas, letrasCertas, palavraSecreta)
                    
                    
                print('Voce excedeu seu limite de palpites')
                print('Voce acertou {} letras e errou {} letras'.format(len(letrasCertas), len(letrasErradas)))
                print('A palavra correta eh: ' + palavraSecreta)
                    
                jogando = False
                    
        if not jogando:
            if playAgain():
                letrasErradas = ''
                letrasCertas = ''
                jogando = True
                
                palavraSecreta = random_word().upper()
                
                    



def printGame(letrasErradas, letrasCertas, palavraSecreta):
    global steps
    print(steps[len(letrasErradas)] + '\n')
    print('Letras erradas', end=' ')
    print_spaces(letrasErradas)
    
    vazio = '_'*len(palavraSecreta)
    
    for i in range(len(palavraSecreta)):
        if palavraSecreta[i] in letrasCertas:
            vazio = vazio[:i] + palavraSecreta[i] + vazio[i+1:]
    
    print_spaces(vazio)        
    
def random_word():
    global palavras
    guessed = random.choice(palavras)
    return guessed

def print_spaces(word):
    for ch in word:
        print(ch, end=' ')
    print()
        
        
def valid_guess(guessList):
    
    while True:
        g = input('Adivinhe uma letra: ').upper()
        
        if len(g) != 1:
            print('Digite apenas um caractere')
        elif g in guessList:
            print('Vc já colocou essa letra!')
        elif not ('A' <= g <= 'Z'):
            print('Apenas letras, por favor!')
        else:
            return g


def playAgain():
    return input('Deseja jogar novamente (sim ou nao)\n').upper().startswith('S')


def verifica_se_ganhou(palavraSecreta, letrasCertas):
    ganhou = True

    for letra in palavraSecreta:
        if letra not in letrasCertas:
            ganhou = False
            break
        
    return ganhou
    
    


main()