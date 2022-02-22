
def split(phrase, sep=' '):
    phraseList = []
    word = ''
    
    i = 0
    
    while i < len(phrase) + 1 - len(sep):
        if phrase[i:i+len(sep)] != sep:
            word += phrase[i]
        else:
            if word != '':
                 phraseList.append(word)
                    
            i += len(sep)
            word = ''
            continue
        
    word += phrase[i:]
    
    if word != '':
        phraseList.append(word)
        
    return phraseList