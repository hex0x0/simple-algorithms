# a=0, b=1.... z=25

TAM_MAX_CH = 26

def cypher(phrase, mode, key):
    global TAM_MAX_CH
    if mode == 'd':
        key *= -1
        
    Translated = '' 
    for symbol in phrase:
        if symbol.isalpha():
            num = ord(symbol)
            num += key
            
            if symbol.isupper():
                if num > ord('Z'):
                    num -= TAM_MAX_CH
                elif num < ord('A'):
                    num += TAM_MAX_CH
                    
            elif symbol.islower():
                if num > ord('z'):
                    num -= TAM_MAX_CH
                elif num < ord('a'):
                    num += TAM_MAX_CH
                    
            Translated += chr(num)
        else:
            Translated += symbol
    return Translated

print(cypher('Eu te amo', 'c', 3))