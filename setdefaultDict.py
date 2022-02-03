
"""

spam ={'color': 'red', 'age': 42}


if 'color' not in spam:
    print('Não existe!')
    spam['color':'black']
else:
    print('Já existe essa chave!')

print(spam)



"""

spam = {'color':'red', 'flag': 'True'}

spam.setdefault('velocity', 234)

print(spam)