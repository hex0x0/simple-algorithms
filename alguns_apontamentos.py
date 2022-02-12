"""

https://www.dropbox.com/sh/t0lvoxb2fxfhctx/AABIYnYyvqPby6oq0NkQWpRaa


"""
def display_intro():

    print(''' Voce acaba de chegar num castelo mal assombrado.
    Você entra. E se depara com uma pessoa muito bem vestida e que convida para entrar.
    
    ''')

play_again = 'yes'


while play_again == 'yes':
    display_intro()

    play_again = input()


hangman_pics = ['''


+-----+
      |
      |
      |
     ===
''',

'''
+-----+
O     |
      |
      |
     === 

''',

'''
+-----+
O     |
|     |
      |
     === 

'''

]

for i in hangman_pics:
    print(i)