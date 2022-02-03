spam = ['apples', 'bananas', 'tofu', 'cats']

objFinal = len(spam) -1

for f in spam:
    
    if f == spam[objFinal]:
        print('and ' + f)
    else:
        print(f, end=' ')