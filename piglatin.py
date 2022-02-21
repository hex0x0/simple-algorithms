#usr/bin/python3

vowels = ('a', 'e', 'i', 'o', 'u')

print('Enter the English message to translate into Pig Latin:')
message = input()

piglatin = []
for word in message.split():
    prefixo = ''

    while len(word) > 0 and not word[0].isalpha():
        prefixo += word[0]
        word = word[1:]

    

    if len(word) == 0:
        piglatin.append(prefixo)
        continue
    
    sufixo = ''
    while  not word[-1].isalpha():
        sufixo += word[-1]
        word = word[:-1]    


    prefixConsonants = ''

    while len(word) > 0 and not word[0] in vowels:
        prefixConsonants += word[0]
        word = word[1:]


    if prefixConsonants != '':
        word += prefixConsonants + 'ay'

    else:
        word += 'yay'

    
    piglatin.append(prefixo + word + sufixo)


print(''.join(piglatin))
    

