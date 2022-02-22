def so_letras(word):
    flag = True
    
    for s in word:
        if not ('a' <= s <= 'z' or 'A' <= s <= 'Z'):
            flag = False
            break
            
    return flag


def apenas_minusculas(word):
    eh_minuscula = True
    for s in word:
        if so_letras(s) and not 'a' <= s <= 'z':
            eh_minuscula = False
            break
    
    return eh_minuscula
    
    
def eh_maiuscula(word):
    eh_maiuscula = True
    
    for s in word:
        if so_letras(s) and not 'A' <= s <= 'Z':
            eh_maiuscula = False
            break
        
    return eh_maiuscula