import sys, pyperclip


text = {'agree': "ok, i'll do it"}

if len(sys.argv) < 2:
    print('Errado')
    sys.exit()
    
    
key = sys.argv[1] 


if key in text:
    pyperclip.copy(text[key])
    print('Text for ' + key + ' copied to clipboard')
    
else:
    print('There is no text for this key')
   
