#string em python são imutáveis

saida = '1 - '

def formata(palavra, lmt, saida):
    if len(palavra) <= lmt:
        saida += palavra + (lmt - len(palavra))*" "
        
    return saida

print(formata('lucas', 16, saida), end=' ')
print('-', end=' ')


