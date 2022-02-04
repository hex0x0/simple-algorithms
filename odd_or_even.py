palavra='josea'

char_central = len(palavra) // 2


print(palavra[char_central])


if not (len(palavra) % 2 == 0):
    print('Eh impar')
else:
    print('Eh par')
